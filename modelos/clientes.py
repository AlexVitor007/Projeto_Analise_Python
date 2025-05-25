from persistent import Persistent

class Cliente(Persistent):
    def __init__(self, id, nome, telefone, cidade, pais):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
        self.pais = pais
