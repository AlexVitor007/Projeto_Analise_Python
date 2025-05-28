from pymongo import MongoClient
from datetime import datetime
import base64

class MongoManager:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="classicmodels_nounstructured"):
        # Inicializa conexão com o MongoDB
        self.client = MongoClient(uri)
        # Seleciona o banco de dados
        self.db = self.client[db_name]
        # Seleciona a coleção de comentários dos clientes
        self.comentarios = self.db["comentarios_clientes"]

    def adicionar_comentario(self, customerNumber, texto, imagem_path=None):
        # Cria um dicionário com o comentário e a data atual UTC
        comentario = {
            "texto": texto,
            "data": datetime.utcnow()
        }

        # Se houver caminho para imagem, abre e codifica a imagem em base64
        if imagem_path:
            with open(imagem_path, "rb") as img:
                encoded = base64.b64encode(img.read()).decode("utf-8")
                comentario["imagem_base64"] = encoded

        # Busca se já existe um registro para o cliente no MongoDB
        cliente = self.comentarios.find_one({"customerNumber": customerNumber})

        if cliente:
            # Se existe, adiciona o novo comentário à lista de comentários
            self.comentarios.update_one(
                {"customerNumber": customerNumber},
                {"$push": {"comentarios": comentario}}
            )
        else:
            # Se não existe, cria um novo documento com o cliente e o comentário
            self.comentarios.insert_one({
                "customerNumber": customerNumber,
                "comentarios": [comentario]
            })

    def listar_comentarios(self, customerNumber):
        # Busca os comentários do cliente no MongoDB
        cliente = self.comentarios.find_one({"customerNumber": customerNumber})
        # Retorna a lista de comentários ou lista vazia se não encontrar
        return cliente["comentarios"] if cliente else []
