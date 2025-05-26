from pymongo import MongoClient
from datetime import datetime
import base64

class MongoManager:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="classicmodels_nounstructured"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.comentarios = self.db["comentarios_clientes"]

    def adicionar_comentario(self, customerNumber, texto, imagem_path=None):
        comentario = {
            "texto": texto,
            "data": datetime.utcnow()
        }

        if imagem_path:
            with open(imagem_path, "rb") as img:
                encoded = base64.b64encode(img.read()).decode("utf-8")
                comentario["imagem_base64"] = encoded
                

        cliente = self.comentarios.find_one({"customerNumber": customerNumber})
        if cliente:
            self.comentarios.update_one(
                {"customerNumber": customerNumber},
                {"$push": {"comentarios": comentario}}
            )
        else:
            self.comentarios.insert_one({
                "customerNumber": customerNumber,
                "comentarios": [comentario]
            })

    def listar_comentarios(self, customerNumber):
        cliente = self.comentarios.find_one({"customerNumber": customerNumber})
        return cliente["comentarios"] if cliente else []
