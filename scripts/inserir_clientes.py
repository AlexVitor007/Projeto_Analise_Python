def inserir():
    from modelos.clientes import Cliente
    import ZODB, ZODB.FileStorage, transaction

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cidade = input("Cidade: ")
    pais = input("País: ")

    storage = ZODB.FileStorage.FileStorage('clientes.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()

    novo = Cliente(len(root['clientes']) + 1, nome, telefone, cidade, pais)
    root['clientes'].append(novo)
    transaction.commit()
    connection.close()
