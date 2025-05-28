# dw/criar_dw.py

import pandas as pd
import sys
import os

# Adiciona a raiz do projeto ao sys.path para permitir imports relativos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa funções de carregamento de dados do banco MySQL
from scripts.importar_mysql import (
    carregar_pedidos,
    carregar_detalhes_pedido,
    carregar_produtos,
    carregar_clientes
)

def criar_data_warehouse():
    """
    Cria um Data Warehouse em memória a partir de dados da base ClassicModels.

    Realiza a junção das tabelas pedidos, detalhes dos pedidos, produtos e clientes,
    e gera as seguintes estruturas:

    - Tabela fato de vendas com dados consolidados de pedidos.
    - Dimensão tempo com ano, mês e dia do pedido.
    - Dimensão produto com código, nome e linha do produto.
    - Dimensão cliente com número, nome e país do cliente.

    Returns:
        tuple: fato_vendas, dim_tempo, dim_produto, dim_cliente
    """

    # Carregamento das tabelas do banco de dados
    pedidos = carregar_pedidos()
    detalhes = carregar_detalhes_pedido()
    produtos = carregar_produtos()
    clientes = carregar_clientes()

    # Junção das tabelas para compor a tabela fato de vendas
    vendas = pedidos.merge(detalhes, on="orderNumber") \
                    .merge(produtos, on="productCode") \
                    .merge(clientes[['customerNumber', 'customerName', 'country']], on="customerNumber")

    # Criação da dimensão tempo
    vendas['orderDate'] = pd.to_datetime(vendas['orderDate'])
    vendas['ano'] = vendas['orderDate'].dt.year
    vendas['mes'] = vendas['orderDate'].dt.month
    vendas['dia'] = vendas['orderDate'].dt.day
    dim_tempo = vendas[['orderDate', 'ano', 'mes', 'dia']].drop_duplicates().reset_index(drop=True)

    # Criação da dimensão produto
    dim_produto = produtos[['productCode', 'productName', 'productLine']].drop_duplicates().reset_index(drop=True)

    # Criação da dimensão cliente
    dim_cliente = clientes[['customerNumber', 'customerName', 'country']].drop_duplicates().reset_index(drop=True)

    # Criação da tabela fato vendas
    fato_vendas = vendas[[
        'orderNumber',
        'orderDate',
        'customerNumber',
        'productCode',
        'quantityOrdered',
        'priceEach'
    ]]

    print("✅ Data Warehouse criado com sucesso em memória!\n")
    return fato_vendas, dim_tempo, dim_produto, dim_cliente


if __name__ == "__main__":
    # Executa a criação do data warehouse e exibe as primeiras linhas de cada estrutura
    fato, tempo, produto, cliente = criar_data_warehouse()

    print("📌 Fato Vendas:")
    print(fato.head(20), "\n")

    print("📌 Dimensão Tempo:")
    print(tempo.head(20), "\n")

    print("📌 Dimensão Produto:")
    print(produto.head(20), "\n")

    print("📌 Dimensão Cliente:")
    print(cliente.head(20), "\n")
