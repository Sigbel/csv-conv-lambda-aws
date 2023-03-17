import boto3
import csv
import os
import sqlite3
import json
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket_name = event['bucket_name']
    object_key = event['object_key']

    try:

        # Download do arquivo CSV do S3
        file_object = s3.get_object(Bucket=bucket_name, Key=object_key)
        file_content = file_object['Body'].read().decode('utf-8').splitlines()
        
        # Tratar as informações do arquivo CSV
        data = []
        reader = csv.DictReader(file_content)
        for row in reader:
            row['cpf'] = row['cpf'].replace('.', '').replace('-', '') # remover a máscara do CPF
            row['cnpj'] = row['cnpj'].replace('.', '').replace('/', '').replace('-', '') # remover a máscara do CNPJ
            row['data'] = datetime.strptime(row['data'], '%d/%m/%Y').strftime('%Y-%m-%d') # formatar data para o padrão yyyy-MM-dd
            data.append(row)
        
        # Conectar ao banco de dados e salvar as informações
        conn = sqlite3.connect(
            database=os.environ['DB_DATABASE']
        )
        cursor = conn.cursor()
        for row in data:
            cursor.execute(
                """
                INSERT INTO minha_tabela (cpf, cnpj, data)
                VALUES (%s, %s, %s)
                """,
                (row['cpf'], row['cnpj'], row['data'])
            )
        conn.commit()
        conn.close()
        
        return {
            'statusCode': 200,
            'body': json.dumps('Dados salvos com sucesso!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro ao processar o arquivo: {str(e)}')
        }
