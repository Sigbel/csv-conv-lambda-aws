<p align="center">
 <h2 align="center">CSV/DataBank - Lambda AWS</h2>
 <p align="center">Leitura e transferência de dados de CSV para um banco de dados.</p>
</p>

<p align="center">
<a href="https://github.com/Sigbel/CSV_Conv_Lambda-AWS/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/sigbel/CSV_Conv_Lambda-AWS?color=0088ff" />
</a>
<a href="https://github.com/Sigbel/Technical_Report_Generator/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/sigbel/CSV_Conv_Lambda-AWS?color=0088ff" />
</a>

</p>
<p align="center">
<a href="#demonstrativo">Ver demonstração</a>
·
<a href="https://github.com/Sigbel/CSV_Conv_Lambda-AWS/issues/new">Reportar erros</a>
·
<a href="https://github.com/Sigbel/CSV_Conv_Lambda-AWS/issues/new">Solicitar recursos</a>
</p>

# Tópicos

- [Cuidados Iniciais](#cuidados-iniciais)
- [Funcionalidades](#funcionalidades)
- [Observações](#observações)

## Cuidados Iniciais

- Clone o repositório com o código da aplicação para o seu computador.
- Antes de prosseguir com a utilização do aplicativo, certifique-se de instalar todas as dependências presentes no arquivo **requirements.txt**.

## Funcionalidades

- Inserção de dados de um arquivo CSV em uma tabela de banco de dados.

## Observações

Para executar a aplicação em um ambiente local, siga as seguintes etapas:

- Defina as variáveis de ambiente necessárias para a conexão com o banco de dados:
    - DB_DATABASE: Nome do banco de dados
- Execute a aplicação com o comando python lambda_function.py.
- Envie uma requisição HTTP com os parâmetros bucket_name e object_key para a URL da sua aplicação. Por exemplo:

Aplicação Local:
~~~~
http://localhost:5000/process-file?bucket_name=my-bucket-name&object_key=my-folder/my-file.csv
~~~~

Exemplo de Aplicação Hospedada:
~~~~
https://6hzzdz2rp3vfjsq2h2vscafiri0axhur.lambda-url.us-east-1.on.aws/bucket_name=my-bucket-name&object_key=my-folder/my-file.csv
~~~~


