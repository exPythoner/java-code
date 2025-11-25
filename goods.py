# coding=utf-8
# @Time : 2025/11/22 14:35
# @File : goods.py
# @Project : git-test-v0

GOODS = ['iPhone', 'iWatch', 'iMac']
for good in GOODS:
    print(f"I will buy {good}")


class GoodSpider:
    def __init__(self, name=None, price=0):
        self.goods_name = name
        self.goods_price = price

    def __str__(self):
        print("print goods info. {}".format(self.goods_name))

    def parse_goods(self):
        print("解析商品信息")

    def run(self):
        for g in GOODS:
            self.__init__(g, 10)
            self.__str__()


if __name__ == '__main__':
    app = GoodSpider()
    app.run()
