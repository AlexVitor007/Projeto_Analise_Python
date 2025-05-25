import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector


# 🔌 Conectar ao MySQL
def conectar_mysql():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="classicmodels"
    )
    return conexao


# 🔄 Carregar dados das tabelas necessárias
def carregar_dados():
    conexao = conectar_mysql()

    pedidos = pd.read_sql("SELECT orderNumber, orderDate FROM orders", conexao)
    detalhes = pd.read_sql("SELECT orderNumber, productCode, quantityOrdered, priceEach FROM orderdetails", conexao)
    produtos = pd.read_sql("SELECT productCode, productName, quantityInStock FROM products", conexao)

    conexao.close()

    if pedidos.empty or detalhes.empty or produtos.empty:
        print("❌ Erro: Uma ou mais tabelas estão vazias.")
        return pd.DataFrame(), pd.DataFrame()

    dados = pd.merge(detalhes, produtos, on="productCode")
    dados = pd.merge(dados, pedidos, on="orderNumber")
    dados['orderDate'] = pd.to_datetime(dados['orderDate'])
    return dados, produtos


# 📊 Histórico de preços
def historico_precos():
    dados, _ = carregar_dados()
    df = dados.groupby(['orderDate', 'productName'])['priceEach'].mean().reset_index()
    tabela = df.pivot(index='orderDate', columns='productName', values='priceEach')
    tabela.plot(figsize=(12,6))
    plt.title("Histórico de Preços por Produto")
    plt.xlabel("Data")
    plt.ylabel("Preço Médio")
    plt.legend(bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()


# 📦 Estoque médio ao longo do tempo
def estoque_medio_temporal():
    dados, produtos = carregar_dados()
    produtos = produtos.set_index('productCode')
    dados['estoque'] = dados['productCode'].map(produtos['quantityInStock'])
    serie = dados.groupby('orderDate')['estoque'].mean()
    serie.plot(figsize=(10,5), title="Estoque Médio ao Longo do Tempo")
    plt.xlabel("Data")
    plt.ylabel("Estoque Médio")
    plt.tight_layout()
    plt.show()


# 🔄 Média móvel de vendas (30 dias)
def media_movel_vendas():
    dados, _ = carregar_dados()
    vendas = dados.groupby('orderDate')['quantityOrdered'].sum()
    vendas_rolagem = vendas.rolling(window=30).mean()
    vendas_rolagem.plot(title='Média Móvel de Vendas (30 dias)', figsize=(10,5))
    plt.xlabel("Data")
    plt.ylabel("Quantidade Vendida (média)")
    plt.tight_layout()
    plt.show()


# 📅 Sazonalidade trimestral
def sazonalidade_trimestral():
    dados, _ = carregar_dados()
    dados['Trimestre'] = dados['orderDate'].dt.to_period('Q')
    total = dados.groupby('Trimestre')['quantityOrdered'].sum()
    total.plot(kind='bar', title='Sazonalidade Trimestral - Quantidade Vendida')
    plt.xlabel("Trimestre")
    plt.ylabel("Quantidade Vendida")
    plt.tight_layout()
    plt.show()


# 📈 Comparativo anual
def comparativo_anual():
    dados, _ = carregar_dados()
    dados['Ano'] = dados['orderDate'].dt.year
    resumo = dados.groupby('Ano').agg({
        'priceEach': 'mean',
        'quantityOrdered': 'sum'
    })
    resumo.plot(kind='bar', figsize=(10,5), title="Comparativo Anual: Preço Médio e Quantidade Vendida")
    plt.ylabel("Valores Médios")
    plt.tight_layout()
    plt.show()
    
    

