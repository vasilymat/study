import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)

x = np.arange(1,15,0.1)
plt.figure()
plt.plot(x,f(x))

xc = np.array([1,4,10,15])
b = f(xc)
a = np.zeros((xc.size,xc.size),dtype='float64')
N = xc.shape[0]
A = np.zeros((N,N),dtype='float64')
i = 0

#Задаем матрицу 
for l in xc:    
    for j in np.arange(N):
        A[i,j]  = l**j
    i += 1

#Получаем коэффициенты при полиноме
X = linalg.solve(A,b)

f2 = x*0
j = 0
for k in X:
    print(k)
    f2 += k*x**j
    j += 1

plt.plot(x,f2)

np.savetxt("C:/MatkivskiyV/study/1_week2/task2.txt",X,fmt='%.2f',newline=' ')
