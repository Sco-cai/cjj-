import xml.dom.minidom
import cv2
from PIL import Image
import os

#——————————————————————————————————————————————————————
width = 0
height = 0
def convert(input_jpg, output_jpg,input_xml,output_xml):
    for filename,filename1 in zip(os.listdir(input_jpg),os.listdir(input_xml)):
        #for filename1 in os.listdir(input_xml):
        path = input_jpg + "/" + filename#获取文件路径
        print("doing picture... ", path)
        ori_img = cv2.imread(path)#读取图片
        height, width = ori_img.shape[:2]
        # 定义缩放信息 以等比例缩放到416为例
        scale = 416 / height
        height = 416
        width = int(width * scale)
        #----------------图片等比例压缩
        img = cv2.resize(ori_img, (width, height))
        cv2.imwrite(output_jpg+'/'+filename, img)

        #for filename in os.listdir(input_xml):
        path1 = input_xml + "/" + filename1  # 获取文件路径
        print("doing xml... ", path1)
        dom = xml.dom.minidom.parse(path1)
        root = dom.documentElement
        # 读取标注目标框
        objects = root.getElementsByTagName("bndbox")
        for object in objects:
            xmin = object.getElementsByTagName("xmin")
            xmin_data = int(float(xmin[0].firstChild.data))
            # xmin[0].firstChild.data =str(int(xmin1 * x))
            ymin = object.getElementsByTagName("ymin")
            ymin_data = int(float(ymin[0].firstChild.data))
            xmax = object.getElementsByTagName("xmax")
            xmax_data = int(float(xmax[0].firstChild.data))
            ymax = object.getElementsByTagName("ymax")
            ymax_data = int(float(ymax[0].firstChild.data))

            # 更新xml
            width_xml = root.getElementsByTagName("width")
            width_xml[0].firstChild.data = width
            height_xml = root.getElementsByTagName("height")
            height_xml[0].firstChild.data = height
            #----------------标签等比例压缩
            xmin[0].firstChild.data = int(xmin_data * scale)
            ymin[0].firstChild.data = int(ymin_data * scale)
            xmax[0].firstChild.data = int(xmax_data * scale)
            ymax[0].firstChild.data = int(ymax_data * scale)
            # 另存更新后的文件
            with open(output_xml + '/' + filename1, 'w') as f:
                dom.writexml(f, addindent='  ', encoding='utf-8')

            #----等比例压缩时要注释下面的代码，该代码只用于验证压缩效果
            #----可以根据保存的图片验证压缩的效果
            left_top = (int(xmin_data*scale), int(ymin_data*scale))
            right_down= (int(xmax_data*scale), int(ymax_data*scale))
            cv2.rectangle(img, left_top, right_down, (255, 0, 0), 1)
            cv2.imwrite('./Annotations_new' +'/'+filename, img)
if __name__ == '__main__':
    #输入路径(根据自己的路径进行设置)
    input_jpg = "G:\\new\\JPG"
    input_xml = "G:\\new\\XML"
    #输出保存路径(根据自己的路径进行设置)
    output_jpg = "G:\\new\\output_jpg"
    output_xml = "G:\\new\\output_xml"
    #调用函数
    convert(input_jpg, output_jpg,input_xml,output_xml)
