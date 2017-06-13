import pandas as pd
import Common.MySQLConnection as ms


class Product(object):

    def __init__(self, statement):
        self.conn = ms.MySQLConnection.get_conn()
        self.statement = statement

    def get_df(self):
        return pd.read_sql(sql=self.statement, con=self.conn)

    def get_product_list(self):
        return self.get_df()["ID"].values

if __name__ == '__main__':
    st = "select * from product"
    x = Product(st)
    print(x.get_product_list())
