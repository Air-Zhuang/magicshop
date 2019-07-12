__author__ = 'GitHub:Air-Zhuang'

# l=[{'id':1,'name':'Air'},{'id':2,'name':'Lucy'},{'id':3,'name':'Bobby'}]
# m=[{'id':1,'num':10},{'id':2,'num':20},{'id':3,'num':30}]
#
#
# n=[{'id':1,'name':'Air','num':10},{'id':2,'name':'Lucy','num':20},{'id':3,'name':'Bobby','num':30}]
#
# lis=[]
# for i in l:
#     for j in m:
#         if j['id']==i['id']:
#             temp={**i,**j}
#             lis.append(temp)
# print(lis)

def a(*args):
    print(args)


def b(fun_name):
    fun_name([1,2])

b