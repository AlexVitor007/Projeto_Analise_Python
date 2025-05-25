# scripts/inicializa_zodb.py
import ZODB, ZODB.FileStorage
import transaction
from modelos.clientes import Cliente

storage = ZODB.FileStorage.FileStorage('clientes.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

root['clientes'] = []

cliente = Cliente(1, "Ana Silva", "1234-5678", "São Paulo", "Brasil")
root['clientes'].append(cliente)

transaction.commit()
connection.close()
