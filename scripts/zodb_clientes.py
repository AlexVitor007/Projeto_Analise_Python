# scripts/zodb_clientes.py
import ZODB, ZODB.FileStorage, transaction
from modelos.clientes import Cliente
from scripts.importar_mysql import carregar_tabela

# Carrega dados da tabela "customers" do banco MySQL
df = carregar_tabela("customers")

# Configura o armazenamento ZODB no arquivo 'clientes.fs'
storage = ZODB.FileStorage.FileStorage('clientes.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

# Inicializa uma lista vazia para armazenar os clientes no ZODB
root['clientes'] = []

# Itera pelas linhas do DataFrame para converter cada linha em objeto Cliente
for _, linha in df.iterrows():
    cliente = Cliente(
        id=linha['Numero'],
        nome=linha['Nome'],
        telefone=linha['Telefone'],
        cidade=linha['Cidade'],
        pais=linha['País']
    )
    root['clientes'].append(cliente)  # Adiciona o objeto cliente ao ZODB

# Salva a transação no banco ZODB
transaction.commit()

# Fecha a conexão com o banco ZODB
connection.close()
