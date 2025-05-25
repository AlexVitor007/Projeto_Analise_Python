import ZODB, ZODB.FileStorage, transaction
from modelos.clientes import Cliente
from scripts.importar_mysql import carregar_clientes

clientes_df = carregar_clientes()

storage = ZODB.FileStorage.FileStorage('clientes.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

root['clientes'] = []

for _, row in clientes_df.iterrows():
    cliente = Cliente(row['customerNumber'], row['customerName'], row['phone'], row['city'], row['country'])
    root['clientes'].append(cliente)
    



transaction.commit()
connection.close()
