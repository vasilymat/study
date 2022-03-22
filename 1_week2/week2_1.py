import numpy as np
import re
from copy import deepcopy
f = open("C:/MatkivskiyV/study/1_week2/week2.txt",'r')
T = []
d1 = {}
list_construct = [0 for i in range(22)]
for x in f:
    x = x.lower().strip() #.нижний_регистр.устранили_пробельные_символы
#    x = x.replace(',','').replace('.','').replace('-','')
    x = re.split('[^a-z]',x) #Эта хрень работает примерно как в перле. Делите-
#   лем является все, что не a-z 
#    x = x.split()
    x = [i for i in x if i != ''] 
    d1.update(dict.fromkeys(x,deepcopy(list_construct) )) #dict construct: for every
    T.append(x)    
f.close()

#Составили табличку из слов/предложений. Всего 22 предложения.
#Напсано, сколько слово встречается в каком из предложений
i = 0
for x in T:
    for x_key in x:
        d1[x_key][i] +=  1
    i += 1
        

#[i for i, e in enumerate([1, 2, 1]) if e == 1] - непонятная хрень
#https://pyneng.readthedocs.io/ru/latest/book/04_data_structures/dict_methods.html 
#    https://webdevblog.ru/kogda-ispolzovat-list-comprehension-v-python/