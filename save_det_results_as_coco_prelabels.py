#coding:utf-8


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import cv2

json_dict = {"images": [], "type": "instances", "annotations": [], "categories": []}
START_BOUNDING_BOX_ID = 1
classes = ['S1', 'S2', 'S3', 'S3', 'S4', 'S5', 'S6']
pre_define_categories = {}
for i, cls in enumerate(classes):
    pre_define_categories[cls] = i + 1

categories = pre_define_categories.copy()
for cate, cid in categories.items():
    cat = {'supercategory': 'none', 'id': cid, 'name': cate}
    json_dict['categories'].append(cat)

def convert(det_results_s, index):
    
    global START_BOUNDING_BOX_ID
    bnd_id = START_BOUNDING_BOX_ID
    
    img_path = det_results_s['file_name']
    width = det_results_s['image_width']
    height = det_results_s['image_height']
    filename = os.path.basename(img_path)[:-4] + ".png"
    image_id = 20190000001 + index

    image = {'file_name': filename, 'height': height, 'width': width, 'id':image_id}
    json_dict['images'].append(image)
    ## Cruuently we do not support segmentation
    #  segmented = get_and_check(root, 'segmented', 1).text
    #  assert segmented == '0'
    det_results = det_results_s['bbox_list']
    length_results = len(det_results)
    #print(len(det_results))
    for det_pos in range(length_results):
        pos = det_results[det_pos]['position']
        xmin,ymin,xmax,ymax = pos[0],pos[1],pos[2],pos[3]
        category_id = det_results[det_pos]['label']     
        o_width = abs(xmax - xmin)
        o_height = abs(ymax - ymin)
        ann = {'area': o_width*o_height, 'iscrowd': 0, 'image_id':
                image_id, 'bbox':[xmin, ymin, o_width, o_height],
                'category_id': category_id, 'id': bnd_id, 'ignore': 0,
                'segmentation': []}
        json_dict['annotations'].append(ann)
        bnd_id = bnd_id + 1
    START_BOUNDING_BOX_ID = bnd_id



def transfer_output_form(image_path,result):
    """
       this fuction is used to transfer the format of detetion results to regulation
    """
    
    image = cv2.imread(image_path)
    #print(image.shape)
    height,width,_ = image.shape
    det_results = result['results']
    #print(len(det_results))
    output_list = []
    for j in range(1, len(det_results) + 1):
        for pos in det_results[j]:
            x0,y0,x1,y1 = int(pos[0]),int(pos[1]),int(pos[2]),int(pos[3])
            score = float(pos[4])
            if score <= 0.3:
               continue
            else:
               output_list.append({'position': [x0,y0,x1,y1], 'label': int(j), 'score': score})
    final_result = {"image_height": height, "image_width": width, "bbox_list": output_list}
    return final_result

