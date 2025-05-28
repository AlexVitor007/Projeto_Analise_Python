from mongoengine import Document, StringField, connect

# Conecta ao banco de dados MongoDB chamado 'classicmodels_mongo' localmente
connect('classicmodels_mongo')

class ComentarioCliente(Document):
    """
    
    Modelo de documento para armazenar comentários de clientes no MongoDB.

    Atributos:
        cliente_id (StringField): Identificador do cliente que fez o comentário.
        comentario (StringField): Texto do comentário realizado pelo cliente.
        
    """
    cliente_id = StringField()
    comentario = StringField()

# Cria e salva um documento ComentarioCliente no banco MongoDB
ComentarioCliente(cliente_id="103", comentario="Muito bom!").save()
