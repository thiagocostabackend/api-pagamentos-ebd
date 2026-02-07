#Responsável pela configuração e conexão com o banco de dados.

import os
import mysql.connector
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def get_connection(): #Cria e retorna uma conexão com o banco de dados MySQL utilizando variáveis de ambiente
    return mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME")
    )
