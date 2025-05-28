import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

def conectar_mysql():
    """
    Estabelece conexão com o banco de dados MySQL 'classicmodels'.

    Retorna:
        conexao (MySQLConnection): Objeto de conexão com o MySQL.
    """
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="classicmodels"
    )
    return conexao


def carregar_dados():
    """
    Carrega dados das tabelas 'orders', 'orderdetails' e 'products' do MySQL.

    Retorna:
        dados (DataFrame): Dados combinados de pedidos, detalhes e produtos.
        produtos (DataFrame): Dados da tabela produtos.
    
    Exibe mensagem de erro e retorna DataFrames vazios caso alguma tabela esteja vazia.
    """
    conexao = conectar_mysql()

    pedidos = pd.read_sql("SELECT orderNumber, orderDate FROM orders", conexao)
    detalhes = pd.read_sql("SELECT orderNumber, productCode, quantityOrdered, priceEach FROM orderdetails", conexao)
    produtos = pd.read_sql("SELECT productCode, productName, quantityInStock FROM products", conexao)

    conexao.close()

    if pedidos.empty or detalhes.empty or produtos.empty:
        print(" Erro: Uma ou mais tabelas estão vazias.")
        return pd.DataFrame(), pd.DataFrame()

    dados = pd.merge(detalhes, produtos, on="productCode")
    dados = pd.merge(dados, pedidos, on="orderNumber")
    dados['orderDate'] = pd.to_datetime(dados['orderDate'])
    return dados, produtos


def historico_precos():
    """
    Gera gráfico de pizza mostrando a distribuição do preço médio dos 20 primeiros produtos.

    O gráfico exibe percentuais e legenda, além da soma total dos preços médios dos produtos selecionados.
    """
    dados, _ = carregar_dados()

    media_precos = dados.groupby('productName')['priceEach'].mean()
    media_precos_20 = media_precos.head(20)
    soma_precos = media_precos_20.sum()

    plt.figure(figsize=(10, 10))
    wedges, texts, autotexts = plt.pie(
        media_precos_20,
        labels=None,
        autopct='%1.1f%%',
        startangle=140
    )

    plt.legend(
        wedges,
        media_precos_20.index,
        title="Produtos",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize='small'
    )

    plt.text(
        1.15, -0.4,
        f"Soma dos preços médios: ${soma_precos:.2f}",
        fontsize=10,
        ha='left'
    )

    plt.title('Distribuição do Preço Médio dos 20 Produtos')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    

def estoque_medio_temporal():
    """
    Plota gráfico da média temporal do estoque médio dos produtos ao longo das datas de pedidos.

    Utiliza a quantidade em estoque do produto e calcula a média diária do estoque dos produtos vendidos.
    """
    dados, produtos = carregar_dados()
    produtos = produtos.set_index('productCode')
    dados['estoque'] = dados['productCode'].map(produtos['quantityInStock'])
    serie = dados.groupby('orderDate')['estoque'].mean()
    serie.plot(figsize=(10,5), title="Estoque Médio ao Longo do Tempo")
    plt.xlabel("Data")
    plt.ylabel("Estoque Médio")
    plt.tight_layout()
    plt.show()


def media_movel_vendas():
    """
    Exibe gráfico da média móvel de vendas diárias ao longo de 30 dias.

    A média móvel suaviza a série temporal da quantidade vendida para evidenciar tendências.
    """
    dados, _ = carregar_dados()
    vendas = dados.groupby('orderDate')['quantityOrdered'].sum()
    vendas_rolagem = vendas.rolling(window=30).mean()
    vendas_rolagem.plot(title='Média Móvel de Vendas (30 dias)', figsize=(10,5))
    plt.xlabel("Data")
    plt.ylabel("Quantidade Vendida (média)")
    plt.tight_layout()
    plt.show()


def sazonalidade_trimestral():
    """
    Gera gráfico de barras para análise de sazonalidade trimestral da quantidade vendida.

    Agrupa vendas por trimestre e apresenta a soma da quantidade vendida em cada trimestre.
    """
    dados, _ = carregar_dados()
    dados['Trimestre'] = dados['orderDate'].dt.to_period('Q')
    total = dados.groupby('Trimestre')['quantityOrdered'].sum()
    total.plot(kind='bar', title='Sazonalidade Trimestral - Quantidade Vendida')
    plt.xlabel("Trimestre")
    plt.ylabel("Quantidade Vendida")
    plt.tight_layout()
    plt.show()


def comparativo_anual():
    """
    Plota gráfico de barras comparativo anual entre preço médio e quantidade vendida.

    Agrupa os dados por ano, calcula média de preço e soma de quantidade vendida.
    """
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
