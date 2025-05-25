from scripts.importar_mysql import carregar_pedidos, carregar_detalhes_pedido, carregar_produtos
import pandas as pd

pedidos = carregar_pedidos()
detalhes = carregar_detalhes_pedido()
produtos = carregar_produtos()

# Fato: vendas
vendas = pedidos.merge(detalhes, on="orderNumber")
vendas = vendas.merge(produtos, on="productCode")
vendas['orderDate'] = pd.to_datetime(vendas['orderDate'])
vendas['ano'] = vendas['orderDate'].dt.year
vendas['mes'] = vendas['orderDate'].dt.month

vendas.to_csv("warehouse/fato_vendas.csv", index=False)
