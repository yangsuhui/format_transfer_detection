# format_transfer_detection
the code to transfer different formats in detection tasks with coco json, yolo txt and voc xml

# format transfer
该程序主要修改CenterNet检测模型推理时使用的demo.py程序，让模型推理后结果直接保存成coco json格式，并可以将
json格式转成voc xml格式。

demo.py：修改的Centernet工程的src/lib/demo.py
save_det_results_as_coco_prelabels.py：将模型的检测结果保存成coco json格式
translate_coco_json_to_xml.py：将coco json转成voc xml格式
CVAT_xml_transfer_voc_xml: 该文件夹下的代码主要用于批量修改图片名称，以及将CVAT标注平台格式的xml转成VOC xml格式
get_corpus_ch_from_html.py：主要将从网络上下载的带有繁体的电子书，小说的html(ebooks_complex_font)直接转成txt文件格式
judge_puntuation.py：主要通过多线程读取大量的OCR标注数据(几十W+级别)，并利用正则表达式判断标注的标点是否正确(中英文标点)

**注意：当用CVAT标注平台时，标注完检测数据后，可以直接下载coco json格式，用CenterNet这种工程的coco.py文件读取
数据就可以；但是当需要将模型推理结果作为预标注上传到CVAT上时，目前测试还是统一成VOC xml格式上传，成功率最大，因此
需要coco json转voc xml格式。**
**CVAT的xml格式主要将一个数据集的所有标注统一存在一个xml文件中，类似于coco json，因此像带有属性的任务(如行人/人脸属性)需要
保存成xml格式，直接从平台下载voc格式的xml会没有属性值，因此CVAT_xml_transfer_voc_xml文件夹下会有CVAT XML格式的读取写法。**

# save_format_cocoeavl
coco.py主要是CenterNet工程下的代码，这里主要说明此处代码中如何将输出结果保存成特定格式用于cocoapi
[评估代码调用](https://yangsuhui.github.io/p/5b87.html)。


# Reference
https://github.com/xingyizhou/CenterNet