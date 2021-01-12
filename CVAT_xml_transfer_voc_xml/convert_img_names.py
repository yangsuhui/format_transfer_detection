#-*- coding: UTF-8 -*-
import os
#filenames = os.listdir(os.getcwd())  
filenames = os.listdir('./total_imgs/') 
for name in filenames:
    print(name)
for num in range(0,len(filenames)):
    if(num<10):
        #print()
        print(filenames[num])
        os.rename(filenames[num],'0'+str(num)+'.png')
    else:
        os.rename(filenames[num],str(num)+'.png')
