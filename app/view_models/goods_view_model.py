__author__ = 'GitHub:Air-Zhuang'

class GoodsCollection:
    def __init__(self, goods):
        self.data = []

        self.__parse(goods)

    def __parse(self, goods):
        for good in goods:
            temp = GoodsViewModel(good)
            self.data.append(temp.data)


class GoodsViewModel:
    def __init__(self, good):
        self.data = {}
        self.data = self.__parse(good)

    def __parse(self, good):
        r = {
            'id':good.id,
            'goods_name': good.goods_name,
            'goods_img': good.goods_img,
            'stock':good.stock,
            'price':str(good.price),
            'goods_detail':good.goods_detail,
            'cpu':good.cpu,
            'ram':good.ram,
            'memory':good.memory,
            'video_card':good.video_card,
            'size':good.size,
            'cate_company':good.cate_company,
            'cate_outlook':good.cate_outlook
        }
        return r
