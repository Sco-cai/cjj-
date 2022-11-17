import os
#将各个文件夹中的图像名称及路径写到txt中
def getFileNames(rootDir,txtpath):
    f=open(txtpath,'w+')
    fileNames = []
    n=0
    # 利用os.walk()函数获取根目录下文件夹名称，子文件夹名称及文件名称
    for dirName, subDirList, fileList in os.walk(rootDir):
        for fname in fileList:
            print("n=",n)
            file_name=dirName + '/' + fname+ '\n'
            f.writelines(file_name)
            fileNames.append(dirName + '/' + fname)
            n=n+1
    return fileNames
 
txtpath="E:/pycharm_workspace/python_data_process/test.txt"
path="E:/pycharm_workspace/python_data_process/pic_argument1/"
aa=getFileNames(path,txtpath)


#某一文件夹单独提取名称及路径
# -*- coding: utf-8 -*-
import os
#用getcwd()获取当前目录
filedir = os.getcwd()+'/pic'
#获取目录列表
filenames=os.listdir(filedir)
#以写的方式打开一个文本
f=open('E:/pycharm_workspace/python_data_process/image.txt','w+')
#for循环
for filename in filenames:
    filepath = filedir+'/'+filename
    dir = filepath + '\n'
    # 把dir写到1.txt文本里面
    f.writelines(dir)
f.close()