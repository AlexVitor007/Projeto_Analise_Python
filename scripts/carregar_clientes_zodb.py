import ZODB, ZODB.FileStorage, transaction
from modelos.clientes import Cliente
from scripts.importar_mysql import carregar_clientes
import pandas as pd

# Carrega dados dos clientes do MySQL usando função auxiliar
clientes_df = carregar_clientes()

# Configura armazenamento do ZODB no arquivo 'clientes.fs'
storage = ZODB.FileStorage.FileStorage('clientes.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

# Inicializa lista vazia para armazenar objetos Cliente no banco ZODB
root['clientes'] = []

# Itera pelas linhas do DataFrame carregado e cria objetos Cliente
for _, row in clientes_df.iterrows():
    cliente = Cliente(
        row['customerNumber'],
        row['customerName'],
        row['phone'],
        row['city'],
        row['country']
    )
    root['clientes'].append(cliente)  # Armazena objeto Cliente na lista do banco

transaction.commit()  # Salva transação no banco
connection.close()    # Fecha conexão com o banco


def carregar_clientes_zodb():
    """
    Carrega dados de clientes armazenados no banco ZODB e retorna um DataFrame.

    Retorna:
        pd.DataFrame: Dados dos clientes lidos do ZODB.
        DataFrame vazio em caso de erro durante a leitura.
    """
    try:
        storage = ZODB.FileStorage.FileStorage('clientes.fs')
        db = ZODB.DB(storage)
        connection = db.open()
        root = connection.root()

        # Recupera lista de objetos Cliente ou lista vazia se não existir
        clientes = root.get('clientes', [])

        # Converte lista de objetos Cliente para lista de dicionários
        data = [{
            'customerNumber': cliente.customerNumber,
            'customerName': cliente.customerName,
            'phone': cliente.phone,
            'city': cliente.city,
            'country': cliente.country
        } for cliente in clientes]

        connection.close()  # Fecha conexão com banco
        return pd.DataFrame(data)  # Retorna DataFrame com dados dos clientes
    
    except Exception as e:
        print(f"Erro ao carregar clientes do ZODB: {e}")
        return pd.DataFrame()  # Retorna DataFrame vazio em caso de erro
