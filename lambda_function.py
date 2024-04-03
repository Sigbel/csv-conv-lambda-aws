import boto3
import csv
import os
import sqlite3
import json
import tempfile
from datetime import datetime

def lambda_handler(event, context):

    s3 = boto3.client('s3')
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    object_key = event['Records'][0]['s3']['object']['key']

    try:
        # Download CSV file from s3
        file_object = s3.get_object(Bucket=bucket_name, Key=object_key)
        
        file_content = file_object['Body'].read().decode('iso-8859-1').splitlines()
        
        # Data treatment
        dataB = []
        reader = csv.reader(file_content, delimiter=';')
        next(reader)

        for row in reader:
            cpf = row[0].replace('.', '').replace('-', '')
            nome = row[1].lower()
            data = datetime.strptime(row[2], '%d/%m/%Y').strftime('%Y-%m-%d')
            dataB.append({'cpf': cpf, 'nome': nome, 'data': data})

        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.sqlite')
        temp_file.close()
        db_path = temp_file.name

        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE minha_tabela (cpf TEXT, nome TEXT, data DATE)
            """
        )
        for row in dataB:
            print(row)
            cursor.execute(
                """
                INSERT INTO minha_tabela (cpf, nome, data)
                VALUES (?, ?, ?)
                """,
                (row['cpf'], row['nome'], row['data'])
            )
        conn.commit()
        conn.close()
        
        # Upload output to s3
        s3.upload_file(db_path, bucket_name, 'output.sqlite')
        
        # Remove temporary file
        os.unlink(db_path)
        
        return {
            'statusCode': 200,
            'body': json.dumps('Arquivo SQLite gerado e enviado para o S3 com sucesso!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro ao processar o arquivo: {str(e)}')
        }