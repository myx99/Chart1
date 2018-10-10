import Common.GlobalConfig as cf


class Product(object):
    def __init__(self):
        self.productID = ''
        self.StartDate = ''
        self.EndDate = ''

    def setProduct(self, product_number):
        self.prodno = product_number

    def getProduct(self):
        config = cf.GlobalConfig()
        self.ProductID = config.getConfig(self.prodno, 'ID')
        self.StartDate = config.getConfig(self.prodno, 'Start_date')
        self.EndDate = config.getConfig(self.prodno, 'End_date')
        return self.ProductID, self.StartDate, self.EndDate


if __name__ == '__main__':
    p = Product()
    p.setProduct('product1')
    q = p.getProduct()
    print(q[0], q[1], q[2])



