#coding:utf-8

import re
import glob
import threading
import time
import os
import math
import json
import csv
import alphabets as alphabets
###编号：2019-009     ###[中文][中文符号][数字]
###- 17 -             ###
###证券简称：大豪科技   ###[中文][中文符号][中文]
###本公司董事会及全体董事保证本公告内容不存在任何虚假记载、误导性陈述
###的，公司应当在公告中作特别提示。
###一、本次限售股上市类型：非公开发行限售股
###月，公司向南通瑞祥针织产业投资合伙企业（有限合伙）（以下简称“南通瑞祥”）
###非公开发行股份3,624,875股，公司于2017年7月20日在中国证券登记结算有限责
###由447,000,000股变更为450,624,875股。2017年12月，公司向北京一轻控股有限责
###任公司、爱慕股份有限公司非公开发行股份合计3,508,480股，公司于2017年12
###2018年5月，公司以资本公积金向全体股东每股转增0.40股，共计转增
###其中，优先级资产支持证券为代表优先级信托受益权的资产支持证券 ，优先级信托受益
###3.债券简称：10沈煤债
###4.债券代码：1080168
###（6）2016 年 8 月 16 日 11 时 10 分许，郑妙慧向公安机关报
###市、县，造成严重后果，或者两次未经批准，擅自离开
###强制缴纳。）
###√属本单位管辖的刑事案件，建议及时立案侦查
###□其他
###*2017年 4 月5日
###VWS2017052551010037130700000769294A0011
###单位及职业//
###审人还应遵守以下规定:
###机关报告；
###成公交（四）送字[2017]10959 号
###录，当事人陈述、检验鉴定书、“天网”监控等。
###2017、06、01
###路发现一辆银色川 A2D15X 号小型轿车与移动警务车相撞和路边
###根据《中华人民共和国刑事诉讼法》第一百一十七条之规
###答：父亲：张清绪，66 岁；母亲：董曼君，61 岁；女儿：张子墨，7
###被讯问人（签名）：
###户籍所在地:四川省成都市青羊区光华村街 55 号
###联系方式：13808187189
###答：2017 年 04 月 04 日晚上，我、张鹏还有其他几个朋友在芳邻路“鹭
###驾驶川 A2D15X号小型轿车在成都市青羊区草堂路发生了交通事故,现

##规则：不对的情况,

# text = "有义务提交各项所需文件；在招标开始后，如遇重大突发性问题，迅速通，"
# text = text.decode("utf-8")
# #[A-Za-z0-9]
# #[\（\）\《\》\——\；\，\。\“\”\<\>\！]
# #[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]
# ##[\·\~\！\@\#\￥\%\……\&\*\（\）\——\-\+\=\【\】\{\}\、\|\；\‘\’\：\“\”\《\》\？\，\。\、]
# r1 = u"[\u4e00-\u9fa5][\（\）\《\》\——\；\，\。\“\”\<\>\！][\u4e00-\u9fa5][\r\n]*"
# r2 = u"[\u4e00-\u9fa5][；，。]"

# text = re.sub(r1, '', text)
# print(text)
# print(re.sub(r2, '', text))

# ##注：中英文 +=-@是不区分的
# text = "有义务提交各项所：需文件：在招标开始后，如遇重大突发性问题，迅，速通，"
# #text = ':我:我,我'
# text = text.decode("utf-8")
# r3 = u"[\u4e00-\u9fa5]*[\`\~\!\#\$\%\^\&\*\(\)\_\[\]\{\}\\\|\;\'\'\:\"\"\,\.\/\<\>\?][\u4e00-\u9fa5][\r\n]*"
# r4 = re.compile(u"[\u4e00-\u9fa5]*[\`\~\!\#\$\%\^\&\*\(\)\_\[\]\{\}\\\|\;\'\'\:\"\"\,\.\/\<\>\?][\u4e00-\u9fa5][\r\n]*")
# a = r4.findall(text)
# ret = re.match(r3,text)
# #print(ret.group())
# print(a)
# for i in a:
#     print(i)
# #print(re.sub(r3, '', text))

"""重新定义带返回值的线程类"""
 
class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
 
    def run(self):
      # 获得锁，成功获得锁定后返回True
      # 可选的timeout参数不填时将一直阻塞直到获得锁定
      # 否则超时后将返回False
        threadLock.acquire()
    #    #线程需要执行的方法
    #    #printImg(self.s,self.e)
    #    #self.result_path,self.result = self.func(*self.args)
    #    self.result = self.func(*self.args)
    #    # 释放锁
    #    threadLock.release()
        self.result = self.func(*self.args)
        print('length of omit character:',len(self.result))

        #threadLock.acquire()

        # with open('omit_character.txt', 'rb') as fin:
        #     omit_label = fin.read().decode('utf8').strip('\n')     
        #     for i_omit_character in self.result:
        #         if i_omit_character in omit_label:
        #             self.result.remove(i_omit_character)
        #         else:
        #             pass

        # txt_w = open('omit_character.txt','a+',encoding='utf-8')
        # for character_ch in self.result:
        #     txt_w.writelines(character_ch)
        #     #txt_w.write('\n')
        # txt_w.close()

        threadLock.release()
        
    def get_result(self):
        try:
           # return self.result_path,self.result
           return self.result
        except Exception:
            return None
 
 
"""测试函数，匹配label"""
def match_punctuation_CN_EN(position_left,position_right):
    # bad_lable_path = []
    # bad_label = []
   # bad_label_dict = {}
    omit_character = []
    #print(position_left,position_right)
    labels_whole = {}
    for path_i in range(position_left,position_right):
        #print('process_label:',path_i)
        label_path = total_label_path[path_i]
        # with open(label_path, 'rb') as fin:
        #     # read().split()结果为一个长度为1的list，所以用[0]提取出string
        #     whole_label = fin.read().decode('utf8').strip('\n').replace(" ", "")
            
        #     #text = text.decode("utf-8")
        #     ##,.:;"()!?
        #     r4 = re.compile(u"[\u4e00-\u9fa5]+[\!\(\)\;\:\"\"\,\.\?][\u4e00-\u9fa5][\r\n]*")
        #     #r4 = re.compile(u"[\u4e00-\u9fa5]+[\`\~\!\#\$\%\^\&\*\(\)\_\[\]\{\}\\\|\;\'\'\:\"\"\,\.\/\<\>\?][\u4e00-\u9fa5][\r\n]*")
        #     a = r4.findall(whole_label)
        #     if len(a) > 0:
        #         #print(whole_label)
        #         # bad_lable_path.append(label_path)
        #         # bad_label.append(whole_label)
        #         bad_label_dict[label_path]=whole_label
        #     else:
        #         pass
    #return bad_lable_path,bad_label
        
        with open(label_path, 'rb') as fin:
            whole_label = fin.read().decode('utf8').strip('\n')
            #labels_whole+=whole_label
            labels_whole[label_path] = whole_label
            for character in whole_label:
                if character not in dict_ch_zh:
                    omit_character.append(character)
                    print('omit character:',character)
                else:
                    pass
                    #print('character:',character)
    print('dict_len:',len(labels_whole.keys()))

    txt_w = open('test.txt','a+',encoding='utf-8')
    for img_i, line_i in labels_whole.items():
        lines = img_i + ' ' + line_i     
        txt_w.writelines(lines)
        txt_w.write('\n')
    # for character_ch in omit_character:
    #     txt_w.writelines(character_ch)
    #     txt_w.write('\n')
    txt_w.close()

    # txt_w = open('omit_character.txt','a+',encoding='utf-8')
    # for character_ch in omit_character:
    #     txt_w.writelines(character_ch)
    #     txt_w.write('\n')
    # txt_w.close()

    return omit_character

    # csv_w = open('bad_label.csv','a+',newline='',encoding='utf-8')
    # writer = csv.writer(csv_w)
    # for key, value in bad_label_dict.items():
    #     writer.writerow([key,value])
    # csv_w.close()

    # return bad_label_dict

        #print(ret.group())

###多线程读取txt文件内容，判断并存储不符合的标注的txt路径
if __name__ == '__main__':
    
    path_list=['./path/train','./path/test']
    train_path_list = ['./s1/train']
    test_path_list = ['./s2/test']
    dict_ch_zh = alphabets.alphabet
    print("origin length of alphabets:",len(dict_ch_zh))

    #print(path_list)
    for path_i in test_path_list:
        start_time = time.time()
        path = os.path.join(path_i,'labels')
        print('path:',path)
        total_label_path = glob.glob(os.path.join(path,'*.txt'))

        totalThread = 32 #需要创建的线程数，可以控制线程的数量

        lenList = len(total_label_path) #列表的总长度
        print('length of label txt:',lenList)
        gap = lenList / totalThread #列表分配到每个线程的执行数
        print('gap:',gap)
        threadLock = threading.Lock() #锁
        threads = [] #创建线程列表

        # 创建新线程和添加线程到列表
        for i in range(totalThread):
            thread = 'thread%s' % i
            if i == 0:
                thread = MyThread(match_punctuation_CN_EN, args=(0,math.floor(gap)))
            elif totalThread==i+1:
                thread = MyThread(match_punctuation_CN_EN, args=(math.floor(i*gap),math.floor(lenList)))
            else:
                thread = MyThread(match_punctuation_CN_EN, args=(math.floor(i*gap),math.floor((i+1)*gap)))
            threads.append(thread) # 添加线程到列表

        # 循环开启线程
        res_bad_label_path=[]
        res_bad_label=[]
        #res = {}
        res = []
        for i in range(totalThread):
            threads[i].start()

        #res=[]
        # 等待所有线程完成
        for t in threads:
            t.join()
            #res.update(t.get_result())
            res.append(t.get_result())
        #     path,label = t.get_result()
        #     res_bad_label_path.extend(path)
        #     res_bad_label.extend(label)
        # print(len(res_bad_label_path))
        # print(res_bad_label_path)
        # print(len(res_bad_label))
        # print(res_bad_label)
       # print(len(res.keys()))
        #print(res.values())
        #print(len(res))
        print("Exiting Main Thread")
        end_time = time.time()
        print('total_time:',end_time-start_time)

        # csv_w = open('bad_label.csv','a+',newline='',encoding='utf-8')
        # writer = csv.writer(csv_w)
        # for key, value in res.items():
        #     writer.writerow([key,value])
        # csv_w.close()


        # li = []
        # for i in range(2):
        #     t = MyThread(match_punctuation_CN_EN, args=(9,1))
        #     li.append(t)
        #     t.start()
        
        
        # res=[]
        # for t in li:
        #     t.join()  # 使用join，防止主线程比子线程跑的快，会拿不到结果
        #     res.append(t.get_result())
        # print(res)
    

 

