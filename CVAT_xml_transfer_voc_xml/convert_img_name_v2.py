#-*- coding: UTF-8 -*-
import os
import xml.etree.ElementTree as ET

# nowDir = os.getcwd()  # 得到进程当前工作目录
# fileList = os.listdir(nowDir)  # 得到进程当前工作目录中的所有文件名称列表
# for fileName in fileList:  # 获取文件列表中的文件
#     if fileName.endswith("xml"):
#         print fileName
#         tree = ET.parse(fileName)
#         root = tree.getroot()

#         for shuink in shuinkList:
#             for child in root:
#                 for sub in child:
#                     if sub.tag == "width" or sub.tag == "height":
#                         sub.text = str(int(sub.text)/shuink)
#                     for subchild in sub:
#                         if subchild.tag == "xmin" or subchild.tag == "xmax" or subchild.tag == "ymin" or subchild.tag == "ymax":
#                             subchild.text = str(int(subchild.text) / shuink)
#             tree.write( fileName)  # 保存修改后的XML文件

# nowDir = os.getcwd()  # 得到进程当前工作目录
# fileList = os.listdir(nowDir)  # 得到进程当前工作目录中的所有文件名称列表

#filenames = os.listdir(os.getcwd())  
filenames_already_biaozhu = os.listdir('./multi_class_detection_old/')
filenames_new = os.listdir('./sample_png/') 
print('filenames_old_length:',len(filenames_already_biaozhu),'filenames_new',len(filenames_new))
print(type(filenames_already_biaozhu))
print(type(filenames_new))
num_error = 0
for name in filenames_already_biaozhu:
    print(name)
    if name in filenames_new:
      filenames_new.remove(name)
    else:
      num_error += 1
      print('num_error:',num_error)
      
print(len(filenames_new))
filename_newid = {}   ##保存的旧的图片名和对应的新图片名

for fileName in filenames_already_biaozhu:  # 获取文件列表中的文件
    num = 0
    if fileName.endswith("xml"):
        print(fileName)
        tree = ET.parse(fileName)
        root = tree.getroot()        
        
        for child in root:
            if child.tag == "filename":
                child.text =   '0'+str(num)+'.png'
                filename_newid[filename.replace('.xml','.png')] = child.text
        num += 1
        
            # for sub in child:
            #     if sub.tag == "width" or sub.tag == "height":
            #         sub.text = str(int(sub.text))
            #     for subchild in sub:
            #         if subchild.tag == "xmin" or subchild.tag == "xmax" or subchild.tag == "ymin" or subchild.tag == "ymax":
            #             subchild.text = str(int(subchild.text))
        tree.write( fileName)  # 保存修改后的XML文件
        os.rename(filename,'0'+str(num)+'.xml')
    print('num_filenames_already_biaozhu:',num)

for num in range(0,len(filenames_already_biaozhu)):
    os.rename(filenames_already_biaozhu[num],filename_newid[filenames_already_biaozhu[num]])


for num in range(len(filenames_already_biaozhu),len(filenames_new)):
    os.rename(filenames[num],str(num)+'.png')
