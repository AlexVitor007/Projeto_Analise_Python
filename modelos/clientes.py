from persistent import Persistent

class Cliente(Persistent):
    def __init__(self, id, nome, telefone, cidade, pais):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
        self.pais = pais


    def __repr__(self):
        return f"{self.nome} - {self.telefone} - {self.cidade}, {self.pais}"