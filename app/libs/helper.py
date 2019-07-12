__author__ = 'GitHub:Air-Zhuang'

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF','jpeg','JPEG'}
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def geneOrderNo():
    import time
    return "".join(str(time.time()).split("."))

def geneGoodsImgName():
    import time
    return "goods_img"+"".join(str(time.time()).split("."))