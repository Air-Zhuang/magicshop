__author__ = 'GitHub:Air-Zhuang'

class OrderCollection:
    def __init__(self, orders):
        self.data = []

        self.__parse(orders)

    def __parse(self, orders):
        for order in orders:
            temp = OrderViewModel(order)
            self.data.append(temp.data)


class OrderViewModel:
    order_status_mapping = {600: "待支付", 601: "待发货", 602: "待收货", 603: "订单关闭"}
    def __init__(self, order):
        self.data = {}
        self.data = self.__parse(order)

    def __parse(self, order):
        r = {
            'id':order.id,
            'order_no':order.order_no,
            'order_status':self.order_status_mapping[order.order_status],
            'order_address': order.order_address,
            'order_detail': order.order_detail,
            'goods_imgs':self.geneList(order.goods_imgs),
            'total_price':str(order.total_price),
        }
        return r

    @staticmethod
    def geneList(s):
        l = []
        for i in s.split(","):
            l.append(i)
        return l
