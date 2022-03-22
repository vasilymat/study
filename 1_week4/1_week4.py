# Файл для работы с каким-нибудь распределением
# https://tvims.nsu.ru/chernova/tv/tv_nsu07.pdf
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
a = 1.5
r = gamma.rvs(a, size=10000)
plt.hist(r,20)