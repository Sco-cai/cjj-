# 帅到包
# 开发时间:2021-09-17  18:32
#最强综合版
import os

path = r"D:\AI\deep-learning-for-image-processing-master\pytorch_object_detection\yolov3_spp\data\重复图片增强\Images"
filename_list = os.listdir(path)
filetype = ".JPG"#文件类型
a = 4669
for i in filename_list:
    used_name = path + '\\' + i
    portion = os.path.splitext(used_name)#将文件名拆成名字和后缀
    if portion[1] == filetype:#检查文件的后缀
        new_name = path + '\\' + 'cell_320-'+ str(a).zfill(4) + '.JPG'  # 文件名长度对齐
        os.rename(used_name, new_name)
    else:pass
    a += 1


