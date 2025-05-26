# scripts/persistir_produtos.py
import ZODB, ZODB.FileStorage, transaction
from modelos.produtos import Produto
from scripts.importar_mysql import carregar_produtos

def persistir_produtos_zodb():
    produtos_df = carregar_produtos()  # Carrega do MySQL (pode ser do seu importar_mysql.py)

    storage = ZODB.FileStorage.FileStorage('zodb/produtos.fs')  # Armazena no diretório zodb
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()

    root['produtos'] = []

    for _, row in produtos_df.iterrows():
        p = Produto(
            row['productCode'],
            row['productName'],
            row['productLine'],
            row['productScale'],
            row['productVendor'],
            row['productDescription'],
            row['quantityInStock'],
            float(row['buyPrice']),
            float(row['MSRP'])
        )
        root['produtos'].append(p)

    transaction.commit()
    connection.close()
