# -*- coding:UTF-8 -*-
import os
import shutil,io

dir_path = "H:/1/duoxiang" ##日志目录
#old_data = '<script type="text/javascript" src="http://m.tiandaoedu.com/Public/scripts/loading.js">' ##旧字符
#new_data = '<!--<script type="text/javascript" src="http://m.tiandaoedu.com/Public/scripts/loading.js">-->' ##新字符
old_data = '题为1关，请收藏当前位置，方便下次学习' ##旧字符
new_data = '' ##新字符

def walkFile(file):
    """
    遍历文件夹
    :param file 遍历文件名称
    :return str
    """
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        i = 0;
        # 遍历文件
        for f in files:
            file = os.path.join(root, f)
            print(file)
            i = i+1;
            alter(file,old_data,new_data,i) #替换字符


            #newdir = os.path.join(root,f[0:-5])
            #new = os.path.join(newdir,'index.html')
            #createflie(file,newdir,new)


def alter(file,old_str,new_str,num):
    #file = unicode(file, "utf8")

    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with io.open(file, "r") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with io.open(file,"w") as f:
        f.write(file_data)
    newname = 'csdx_'.str(num)
    os.rename(file, newname)

def createflie(file,newdir,new):
    try:
        os.mkdir(newdir)
        shutil.move(file, new)
        os.unlink(file)
    except:
        print(new)

def main():
    walkFile(dir_path)

if __name__ == '__main__':
    main()