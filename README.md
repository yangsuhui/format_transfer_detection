# format_transfer_detection
the code to transfer different formats in detection tasks with coco json, yolo txt and voc xml

# format transfer
该程序主要修改CenterNet检测模型推理时使用的demo.py程序，让模型推理后结果直接保存成coco json格式，并可以将
json格式转成voc xml格式。

demo.py：修改的Centernet工程的src/lib/demo.py
save_det_results_as_coco_prelabels.py：将模型的检测结果保存成coco json格式
translate_coco_json_to_xml.py：将coco json转成voc xml格式

# save_format_cocoeavl
coco.py主要是CenterNet工程下的代码，这里主要说明此处代码中如何将输出结果保存成特定格式用于cocoapi
[评估代码调用](https://yangsuhui.github.io/p/5b87.html)。


# Reference
https://github.com/xingyizhou/CenterNet