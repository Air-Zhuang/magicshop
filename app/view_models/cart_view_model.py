__author__ = 'GitHub:Air-Zhuang'

class CartCollection:
    def __init__(self, carts):
        self.data = []

        self.__parse(carts)

    def __parse(self, carts):
        for cart in carts:
            temp = CartViewModel(cart)
            self.data.append(temp.data)


class CartViewModel:
    def __init__(self, cart):
        self.data = {}
        self.data = self.__parse(cart)

    def __parse(self, cart):
        r = {
            'id':cart.id,
            'gid':cart.gid,
            'num':cart.num,
            'goods_name': cart.goods_name,
            'goods_img': cart.goods_img,
            'price':str(cart.price),
            'cpu':cart.cpu,
            'ram':cart.ram,
            'memory':cart.memory,
            'video_card':cart.video_card,
            'size':cart.size,
            'cate_company':cart.cate_company,
            'total_price':str(cart.total_price)
        }
        return r
