# scripts/zodb_clientes.py
import ZODB, ZODB.FileStorage, transaction
from modelos.clientes import Cliente
from scripts.importar_mysql import carregar_tabela

df = carregar_tabela("customers")

storage = ZODB.FileStorage.FileStorage('clientes.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

root['clientes'] = []

for _, linha in df.iterrows():
    cliente = Cliente(
        id=linha['customerNumber'],
        nome=linha['customerName'],
        telefone=linha['phone'],
        cidade=linha['city'],
        pais=linha['country']
    )
    root['clientes'].append(cliente)

transaction.commit()
connection.close()
