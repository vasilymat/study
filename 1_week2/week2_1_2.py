import numpy as np
import re
#from copy import deepcopy
from scipy.spatial.distance import cosine
f = open("C:/MatkivskiyV/study/1_week2/week2.txt",'r')
T = []
d1 = {}
i = 0
for x in f:
    x = x.lower().strip() #.нижний_регистр.устранили_пробельные_символы
#    x = x.replace(',','').replace('.','').replace('-','')
    x = re.split('[^a-z]',x) #Эта хрень работает примерно как в перле. Делите-
#   лем является все, что не a-z 
#    x = x.split()
    x = [i for i in x if i != ''] # delete all whitespaces
    for y in x:
        if d1.setdefault(y) == None:
           d1[y] = i
           i += 1
    T.append(x)
    
f.close()

list_tmp = [0 for i in range(len(d1))]
D = [list_tmp.copy() for j in range(len(T))]

D1 = np.zeros((len(T),len(d1)),dtype='int32')

#Составили табличку из слов/предложений. Всего 22 предложения.
#Напсано, сколько слово встречается в каком из предложений
i = 0
for x in T:
    for x_key in x:
        D1[i][d1[x_key]] +=  1
    i += 1

Cos_dist = np.array([np.round(cosine(D1[0],D1[i]),2) for i in range(len(T))])
np.savetxt("C:/MatkivskiyV/study/1_week2/task1.txt",
           Cos_dist.argsort()[1:3],fmt='%i',newline=' ')
f = open("C:/MatkivskiyV/study/1_week2/task1.txt",'r')
print(f.readline())
f.close()
    
#Cos_dist = [np.round(cosine(D1[0],D1[i]),2) for i in range(len(T))]
#f = open("C:/MatkivskiyV/study/1_week2/task1.txt",'w')
#f.writelines(Cos_dist)
#f.close()
        

#[i for i, e in enumerate([1, 2, 1]) if e == 1] - непонятная хрень
#https://pyneng.readthedocs.io/ru/latest/book/04_data_structures/dict_methods.html 
#    https://webdevblog.ru/kogda-ispolzovat-list-comprehension-v-python/