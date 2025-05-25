# dw/criar_dw.py

import pandas as pd
import sys
import os

# Adicionar a raiz do projeto ao sys.path para permitir imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.importar_mysql import (
    carregar_pedidos,
    carregar_detalhes_pedido,
    carregar_produtos,
    carregar_clientes
)

def criar_data_warehouse():
    # Carregamento das tabelas
    pedidos = carregar_pedidos()
    detalhes = carregar_detalhes_pedido()
    produtos = carregar_produtos()
    clientes = carregar_clientes()

    # Fato: vendas (integra pedidos + detalhes + produtos + clientes)
    vendas = pedidos.merge(detalhes, on="orderNumber") \
                    .merge(produtos, on="productCode") \
                    .merge(clientes[['customerNumber', 'customerName', 'country']], on="customerNumber")

    # Dimensão Tempo
    vendas['orderDate'] = pd.to_datetime(vendas['orderDate'])
    vendas['ano'] = vendas['orderDate'].dt.year
    vendas['mes'] = vendas['orderDate'].dt.month
    vendas['dia'] = vendas['orderDate'].dt.day

    dim_tempo = vendas[['orderDate', 'ano', 'mes', 'dia']].drop_duplicates().reset_index(drop=True)

    # Dimensão Produto
    dim_produto = produtos[['productCode', 'productName', 'productLine']].drop_duplicates().reset_index(drop=True)

    # Dimensão Cliente
    dim_cliente = clientes[['customerNumber', 'customerName', 'country']].drop_duplicates().reset_index(drop=True)

    # Fato Vendas
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
    fato, tempo, produto, cliente = criar_data_warehouse()

    print("📌 Fato Vendas:")
    print(fato.head(20), "\n")
    
    #A tabela fato guarda os eventos de vendas, ou seja, cada linha representa uma venda de 
    # um produto por um cliente em uma data específica.
    #Contém medidas quantitativas (como quantidade vendida e preço por unidade).

    print("📌 Dimensão Tempo:")
    print(tempo.head(20), "\n")
    
    #Tabelas com dados descritivos que complementam a tabela fato.
    

    print("📌 Dimensão Produto:")
    print(produto.head(20), "\n")
    
    

    print("📌 Dimensão Cliente:")
    print(cliente.head(20), "\n")
