import pandas as pd
import matplotlib.pyplot as plt
from scripts.importar_mysql import carregar_pedidos, carregar_detalhes_pedido

def gerar_grafico():
    pedidos = carregar_pedidos()
    detalhes = carregar_detalhes_pedido()

    df = pedidos.merge(detalhes, on="orderNumber")
    df['orderDate'] = pd.to_datetime(df['orderDate'])
    df['ano'] = df['orderDate'].dt.year

    resumo = df.groupby("ano")["quantityOrdered"].sum()

    resumo.plot(kind="bar", title="Tendência de Vendas por Ano")
    plt.xlabel("Ano")
    plt.ylabel("Quantidade de Produtos Vendidos")
    plt.tight_layout()
    plt.show()

