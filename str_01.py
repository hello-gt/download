# -*- coding:UTF-8 -*-
import os
import shutil,io

dir_path = "H:/公务员/常识判断/常识多项/1/danxiang" ##日志目录
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
        # 遍历文件
        for f in files:
            file = os.path.join(root, f)
            with open(file, 'r') as f:
                print(f.read())
            exit()

def main():
    walkFile(dir_path)

if __name__ == '__main__':
    main()