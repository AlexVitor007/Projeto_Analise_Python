from mongoengine import Document, StringField, connect

connect('classicmodels_mongo')

class ComentarioCliente(Document):
    cliente_id = StringField()
    comentario = StringField()

ComentarioCliente(cliente_id="103", comentario="Muito bom!").save()