import numpy as np

incomes = np.random.normal(27000,15000,10000)
incomes = np.append(incomes,[100000000])
print('mean=',np.mean(incomes))
print('median=',np.median(incomes))

# give a random age matrix
ages = np.random.randint(18,high=99,size=30)
print(ages)
from scipy import stats
# give out the most common number that appears in the ages matix and how many times
stats.mode(ages)
print(stats.mode(ages))

#import matplotlib.pyplot as plt
#plt.hist(incomes,50)
#plt.show()

