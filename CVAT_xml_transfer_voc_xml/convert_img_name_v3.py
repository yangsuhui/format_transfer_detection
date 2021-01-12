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
    if name.replace('.xml','.png') in filenames_new:
      filenames_new.remove(name.replace('.xml','.png'))
    else:
      num_error += 1
      print('num_error:',num_error)
      
print(len(filenames_new))
filename_newid = {}   ##保存的旧的图片名和对应的新图片名

cvat_xml_filename = r'./multi_class_detection_example.xml'
tree_cvat_xml = ET.parse(cvat_xml_filename)
root_cvat_xml = tree_cvat_xml.getroot()  

num = -1
for fileName in filenames_already_biaozhu:  # 获取文件列表中的文件
    if fileName.endswith("xml"):
        print(fileName)
        tree = ET.parse(fileName)
        root = tree.getroot()        
        num += 1

        flag = False
        bbox_s = []
        for child_s in root_cvat_xml:
            if child_s.tag == "image":
                if fileName.replace('.xml','.png') in child_s.attrib["name"]:
                    flag = True
                    for sub in child_s:
                        bbox_item = [sub.attrib["xtl"], sub.attrib["ytl"], sub.attrib("xbr"), sub.attrib("ybr")]
                        for subchild in sub:
                            bbox_item.extend(subchild.text)
                        bbox_s.append(bbox_item)

        num_i = 0
        for child in root:
            if child.tag == "filename":
                child.text =  '0'+str(num)+'.png'
                filename_newid[fileName.replace('.xml','.png')] = child.text        
            for sub in child:
                if sub.tag == 'name':
                    sub.text = bbox_s[num_i][4]
                for subchild in sub:
                    if subchild.tag == "xmin":
                        subchild.text = bbox_s[num_i][0]
                    if subchild.tag == "ymin":
                        subchild.text = bbox_s[num_i][1]
                    if subchild.tag == "xmax":
                        subchild.text = bbox_s[num_i][2]
                    if subchild.tag == "ymax":
                        subchild.text = bbox_s[num_i][3]
                num_i += 1
                        

        tree.write( fileName)  # 保存修改后的XML文件
        os.rename(fileName,'0'+str(num)+'.xml')
    print('num_filenames_already_biaozhu:',num)
print('num:',num)
for num in range(0,len(filenames_already_biaozhu)):
    os.rename(filenames_already_biaozhu[num].replace('.xml','.png'),filename_newid[filenames_already_biaozhu[num].replace('.xml','.png')])


for num in range(0,len(filenames_new)):
    os.rename(filenames_new[num],str(num + len(filenames_already_biaozhu))+'.png')

