# -*- coding:UTF-8 -*-
import os
import shutil,io

dir_path = "F:/lgt/svn/m.tiandaoedu.com/public/yxk/" ##日志目录
#old_data = '<script type="text/javascript" src="http://m.tiandaoedu.com/Public/scripts/loading.js">' ##旧字符
#new_data = '<!--<script type="text/javascript" src="http://m.tiandaoedu.com/Public/scripts/loading.js">-->' ##新字符
old_data = 'http://m.tiandaoedu.com/Public' ##旧字符
new_data = 'http://m.tiandaoedu.com/topic_public' ##新字符

#old_data = '<a href="http://u.tiandaoedu.com/denglu.html?from=http://m.tiandaoedu.com/yxk/bk-all-all-tj/" style="margin:10px 5px;color:white;">登录/注册</a>' ##旧字符
#new_data = '' ##新字符

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

        # 遍历文件
        for f in files:
            file = os.path.join(root, f)
            print(file)
            alter(file,old_data,new_data) #替换字符


            #newdir = os.path.join(root,f[0:-5])
            #new = os.path.join(newdir,'index.html')
            #createflie(file,newdir,new)


def alter(file,old_str,new_str):
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