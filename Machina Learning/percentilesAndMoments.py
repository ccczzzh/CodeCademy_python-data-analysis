#percentiles: in a data set, what's the point at
#which X% of the values are less than that value

import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0,0.5,10000)

print('percentile of 50% : ',np.percentile(vals,50))
print('percentile of 90% : ',np.percentile(vals,90))
print('percentile of 20% : ',np.percentile(vals,20))

#plt.hist(vals,50)
#plt.show()

#moments: quantitative measures of the "shape" of a
#probability density function
# first moment is the mean, second moment is the variance

import numpy as np
import matplotlib.pyplot as plt
#vals = np.random.normal(0,0.5,10000)
#first moment
print('first moment : ',np.mean(vals))
#second moment
print('second moment : ',np.var(vals))
#third moment
import scipy.stats as sp
print('third moment : ',sp.skew(vals))
#forth moment
print('forth moment : ',sp.kurtosis(vals))