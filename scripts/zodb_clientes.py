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
        id=linha['Numero'],
        nome=linha['Nome'],
        telefone=linha['Telefone'],
        cidade=linha['Cidade'],
        pais=linha['País']
    )
    root['clientes'].append(cliente)

transaction.commit()
connection.close()
