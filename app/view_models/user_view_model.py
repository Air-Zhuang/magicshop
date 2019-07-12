__author__ = 'GitHub:Air-Zhuang'

class UserViewModel:
    def __init__(self, user):
        self.data = {}
        self.data = self.__parse(user)

    def __parse(self, user):
        r = {
            'id':user.id,
            'nickname': user.nickname,
            'phone_number': user.phone_number,
            'email':user.email,
            'address':user.address,
            'user_img':user.user_img,
        }
        return r
