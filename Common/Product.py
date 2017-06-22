import Common.ProductList as pl


class Product(object):
    def __init__(self):
        self.id = ""
        self.start_nav_date = ""

    def setID(self, ID):
        self.id = ID

    def setStartNavDate(self, sndate):
        self.start_nav_date = sndate

    def getID(self):
        return self.id

    def getStartNavDate(self):
        return self.start_nav_date

if __name__ == '__main__':
    plist = pl.ProductList()
    df = plist.getProductTable()
    p = Product()
    p.setID(df.iloc[0]["ID"])
    p.setStartNavDate(df.iloc[0]["Start_Nav_Date"])
    print(p.getID())
    print(p.getStartNavDate())
