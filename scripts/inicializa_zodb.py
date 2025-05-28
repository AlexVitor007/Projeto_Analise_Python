import ZODB
import ZODB.FileStorage
import transaction
from modelos.clientes import Cliente

# Cria um storage baseado em arquivo para persistência dos dados dos clientes
storage = ZODB.FileStorage.FileStorage('clientes.fs')

# Inicializa o banco de dados ZODB usando o storage criado
db = ZODB.DB(storage)

# Abre uma conexão com o banco
connection = db.open()

# Obtém o objeto raiz da conexão, onde os dados serão armazenados
root = connection.root()

# Inicializa a lista 'clientes' no banco como uma lista vazia
root['clientes'] = []

# Confirma (commita) a transação para salvar a modificação no banco
transaction.commit()

# Fecha a conexão com o banco
connection.close()
