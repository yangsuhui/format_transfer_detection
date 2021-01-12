# -*- coding: utf-8 -*-
import html2text
from lxml import etree
import glob
import os
import sys

path = r'./ebooks_complex_font'
num = 0
old=sys.stdout
for html_path_i in glob.glob(os.path.join(path,'*','*','*.xhtml'),recursive=True):
    num+=1
    sys.stdout=old 
    print(num,html_path_i)
    f = open(html_path_i,"r",encoding="utf-8")
    f = f.read()
    text = html2text.html2text(f)
    save_path = os.path.join(path,str(num)+'.txt')
    txt_w = open(save_path,'w',encoding="utf-8")
    sys.stdout=txt_w    
    print(text)
    txt_w.close()

