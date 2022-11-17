import os
import shutil
 
#测试列表
name_list=open('./2008_test.txt')
#图片路径
tu_dir='./VOC2008/JPEGImages'
#保存路径
save='./test'
dir_name = []
#获取文件名
for i in name_list:
    dir_name.append(os.path.basename(i.replace('\n','')))
#print(dir_name)
#批量复制
for i in dir_name:
    shutil.copy(tu_dir+'/'+i,save+'/'+i)