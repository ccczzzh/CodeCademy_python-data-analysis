import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100,200,10000)

#plt.hist(incomes,50)
#plt.show()
print(incomes)
incomesMean = np.mean(incomes)
print(incomesMean)
incomesMedian = np.median(incomes)
print(incomesMedian)

from scipy import stats

print(stats.mode(incomes))