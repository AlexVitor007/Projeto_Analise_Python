import ZODB, ZODB.FileStorage, transaction
from modelos.clientes import Cliente
from scripts.importar_mysql import carregar_clientes
import ZODB, ZODB.FileStorage
import pandas as pd

clientes_df = carregar_clientes()

storage = ZODB.FileStorage.FileStorage('clientes.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

root['clientes'] = []

for _, row in clientes_df.iterrows():
    cliente = Cliente(row['customerNumber'], row['customerName'], row['phone'], row['city'], row['country'])
    root['clientes'].append(cliente) # conversão em objeto
    



transaction.commit()
connection.close()



def carregar_clientes_zodb():
    try:
        storage = ZODB.FileStorage.FileStorage('clientes.fs')
        db = ZODB.DB(storage)
        connection = db.open()
        root = connection.root()

        clientes = root.get('clientes', [])

        data = [{
            'customerNumber': cliente.customerNumber,
            'customerName': cliente.customerName,
            'phone': cliente.phone,
            'city': cliente.city,
            'country': cliente.country
        } for cliente in clientes]

        connection.close()
        return pd.DataFrame(data)
    

    except Exception as e:
        print(f"Erro ao carregar clientes do ZODB: {e}")
        return pd.DataFrame()

    

