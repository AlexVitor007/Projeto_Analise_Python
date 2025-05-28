import mysql.connector
import pandas as pd

def conectar_mysql():
    """
    Estabelece conexão com o banco de dados MySQL 'classicmodels'.

    Returns:
        mysql.connector.connection.MySQLConnection: Objeto de conexão ativo com o banco.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="classicmodels"
    )


def carregar_tabela(nome_tabela):
    """
    Carrega dados de uma tabela específica do banco 'classicmodels' em um DataFrame.

    Args:
        nome_tabela (str): Nome da tabela a ser carregada.

    Returns:
        pandas.DataFrame: Dados carregados da tabela.
    """
    conexao = conectar_mysql()
    df = pd.read_sql(f"SELECT * FROM {nome_tabela}", conexao)
    conexao.close()
    return df


def carregar_clientes():
    """
    Carrega dados da tabela 'customers', ordenando pelo 'customerNumber' decrescente.

    Returns:
        pandas.DataFrame: Dados dos clientes ordenados do mais recente para o mais antigo.
    """
    conexao = conectar_mysql()
    df = pd.read_sql("SELECT * FROM customers ORDER BY customerNumber DESC", conexao)
    conexao.close()
    return df


def carregar_pedidos():
    """
    Carrega dados da tabela 'orders'.

    Returns:
        pandas.DataFrame: Dados dos pedidos.
    """
    return carregar_tabela("orders")


def carregar_produtos():
    """
    Carrega dados da tabela 'products'.

    Returns:
        pandas.DataFrame: Dados dos produtos.
    """
    return carregar_tabela("products")


def carregar_detalhes_pedido():
    """
    Carrega dados da tabela 'orderdetails'.

    Returns:
        pandas.DataFrame: Dados dos detalhes dos pedidos.
    """
    return carregar_tabela("orderdetails")


def carregar_funcionarios():
    """
    Carrega dados da tabela 'employees'.

    Returns:
        pandas.DataFrame: Dados dos funcionários.
    """
    return carregar_tabela("employees")
