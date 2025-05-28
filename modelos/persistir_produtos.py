# scripts/persistir_produtos.py

import ZODB, ZODB.FileStorage, transaction
from modelos.produtos import Produto
from scripts.importar_mysql import carregar_produtos

def persistir_produtos_zodb():
    """
    Persiste os produtos carregados do banco de dados MySQL em um banco de dados orientado a objetos (ZODB).

    Etapas:
    1. Carrega os produtos a partir da função `carregar_produtos` do módulo importar_mysql.
    2. Cria/abre um banco de dados ZODB armazenado no arquivo 'zodb/produtos.fs'.
    3. Inicializa ou sobrescreve a lista de produtos no root do banco ZODB.
    4. Itera sobre cada linha do DataFrame de produtos e cria uma instância da classe Produto.
    5. Armazena cada instância na lista 'produtos' do root.
    6. Comita a transação e fecha a conexão com o banco ZODB.
    
    """
    
    # Carrega os dados dos produtos do banco MySQL
    produtos_df = carregar_produtos()

    # Configura o armazenamento físico do ZODB no caminho especificado
    storage = ZODB.FileStorage.FileStorage('zodb/produtos.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()

    # Cria (ou sobrescreve) uma lista de produtos no root do banco
    root['produtos'] = []

    # Itera pelas linhas do DataFrame e converte cada linha em um objeto Produto
    for _, row in produtos_df.iterrows():
        p = Produto(
            row['productCode'],          # Código do produto
            row['productName'],          # Nome do produto
            row['productLine'],          # Linha do produto
            row['productScale'],         # Escala do produto
            row['productVendor'],        # Fornecedor
            row['productDescription'],   # Descrição
            row['quantityInStock'],      # Quantidade em estoque
            float(row['buyPrice']),      # Preço de compra
            float(row['MSRP'])           # Preço sugerido ao consumidor
        )
        # Adiciona o produto à lista persistida
        root['produtos'].append(p)

    # Comita as alterações no banco ZODB
    transaction.commit()
    # Encerra a conexão com o banco
    connection.close()
