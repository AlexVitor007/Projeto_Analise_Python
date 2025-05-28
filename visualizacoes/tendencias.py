import pandas as pd
import matplotlib.pyplot as plt
from scripts.importar_mysql import carregar_pedidos, carregar_detalhes_pedido

def gerar_grafico():
    # Carrega dados de pedidos e detalhes dos pedidos do MySQL
    pedidos = carregar_pedidos()
    detalhes = carregar_detalhes_pedido()

    # Faz merge das tabelas pelo número do pedido
    df = pedidos.merge(detalhes, on="orderNumber")

    # Converte a coluna 'orderDate' para datetime
    df['orderDate'] = pd.to_datetime(df['orderDate'])

    # Extrai o ano da data do pedido
    df['ano'] = df['orderDate'].dt.year

    # Agrupa por ano e soma a quantidade de produtos vendidos
    resumo = df.groupby("ano")["quantityOrdered"].sum()

    # Plota gráfico de barras mostrando a tendência de vendas por ano
    resumo.plot(kind="bar", title="Tendência de Vendas por Ano")
    plt.xlabel("Ano")
    plt.ylabel("Quantidade de Produtos Vendidos")
    plt.tight_layout()
    plt.show()
