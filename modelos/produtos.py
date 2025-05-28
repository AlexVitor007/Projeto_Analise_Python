# modelos/produtos.py

class Produto:
    """
    
    Classe que representa a entidade Produto no sistema.

    Esta classe é utilizada para modelar os produtos do banco de dados ClassicModels
    e permite sua persistência no banco de dados orientado a objetos ZODB.

    Atributos:
        productCode (str): Código único do produto.
        productName (str): Nome do produto.
        productLine (str): Linha ou categoria do produto.
        productScale (str): Escala do produto (por exemplo, 1:18).
        productVendor (str): Fornecedor do produto.
        productDescription (str): Descrição detalhada do produto.
        quantityInStock (int): Quantidade disponível em estoque.
        buyPrice (float): Preço de compra do produto.
        MSRP (float): Preço sugerido ao consumidor (Manufacturer's Suggested Retail Price).
        
    """

    def __init__(self, productCode, productName, productLine, productScale, productVendor,
                 productDescription, quantityInStock, buyPrice, MSRP):
        # Inicialização dos atributos da instância com os dados recebidos
        self.productCode = productCode
        self.productName = productName
        self.productLine = productLine
        self.productScale = productScale
        self.productVendor = productVendor
        self.productDescription = productDescription
        self.quantityInStock = quantityInStock
        self.buyPrice = buyPrice
        self.MSRP = MSRP

    def __repr__(self):
        """
        Representação informal do objeto Produto.
        Retorna uma string com o código e nome do produto.
        """
        return f"<Produto {self.productCode} - {self.productName}>"
