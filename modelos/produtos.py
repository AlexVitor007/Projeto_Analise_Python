# modelos/produtos.py

class Produto:
    def __init__(self, productCode, productName, productLine, productScale, productVendor,
                 productDescription, quantityInStock, buyPrice, MSRP):
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
        return f"<Produto {self.productCode} - {self.productName}>"
