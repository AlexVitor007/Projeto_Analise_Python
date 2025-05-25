import mysql.connector
import pandas as pd

# Conecta ao banco ClassicModels
def conectar_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="classicmodels"
    )
    
    

# Comando reutilizável para carregar qualquer tabela
def carregar_tabela(nome_tabela):
    conexao = conectar_mysql()
    df = pd.read_sql(f"SELECT * FROM {nome_tabela}", conexao)
    conexao.close()
    return df

# Comandos úteis (exemplos prontos)
def carregar_clientes():
    return carregar_tabela("customers")

def carregar_pedidos():
    return carregar_tabela("orders")

def carregar_produtos():
    return carregar_tabela("products")

def carregar_detalhes_pedido():
    return carregar_tabela("orderdetails")

def carregar_funcionarios():
    return carregar_tabela("employees")
