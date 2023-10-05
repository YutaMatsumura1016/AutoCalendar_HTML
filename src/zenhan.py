# 全角撲滅
def zenhan(day):
    zen = "０１２３４５６７８９／（）、～　"
    han = "0123456789/(),~ "
    dic = dict(zip(zen, han))
    res = ''.join(dic.get(d, d) for d in day)
    return res