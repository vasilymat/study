import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)

def fm(x):
    return np.int32( np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2) )

x = np.arange(1,30,0.1)
plt.figure()
plt.plot(x,f(x))

result = np.zeros(5)

tmp = optimize.minimize(f,(2),method='BFGS')
result[0] = tmp.fun
tmp = optimize.minimize(f,(30),method='BFGS')
result[1] = tmp.fun

tmp = optimize.differential_evolution(f,[(1,30)])
result[2] = tmp.fun


tmp = optimize.minimize(fm,(30),method='BFGS')
result[3] = tmp.fun
tmp = optimize.differential_evolution(fm,[(1,30)])
result[4] = tmp.fun

np.savetxt("C:/MatkivskiyV/study/1_week3/task1.txt",result,
           fmt='%.2f',newline=' ')
