from persistent import Persistent

class Cliente(Persistent):
    """
    Classe que representa um cliente e herda de Persistent para persistência no ZODB.

    Atributos:
        id (int): Identificador único do cliente.
        nome (str): Nome do cliente.
        telefone (str): Número de telefone do cliente.
        cidade (str): Cidade onde o cliente reside.
        pais (str): País onde o cliente reside.
    """

    def __init__(self, id, nome, telefone, cidade, pais):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
        self.pais = pais

    def __repr__(self):
        """
        Representação em string do objeto Cliente.

        Retorna:
            str: String formatada com nome, telefone, cidade e país do cliente.
        """
        return f"{self.nome} - {self.telefone} - {self.cidade}, {self.pais}"
