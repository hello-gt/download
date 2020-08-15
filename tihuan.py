import os

path = input('H:/公务员/常识判断/常识多项/1/')

# 获取该目录下所有文件，存入列表中
f = os.listdir(path)

n = 0
for i in f:
    # 设置旧文件名（就是路径+文件名）
    oldname = path + f[n]
    uipath = unicode(oldname, "utf8")

    # 设置新文件名
    newname = path + 'a' + str(n + 1) + '.html'

    # 用os模块中的rename方法对文件改名
    os.rename(uipath, newname)
    print(uipath, '======>', newname)

    n += 1