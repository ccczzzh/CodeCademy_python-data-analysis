import numpy as np
import matplotlib.pyplot as plt
#===============================
# Uniform distribution
#================================
values = np.random.uniform(-10,10,10000)
#plt.hist(values,50)
#plt.show()
#=============================
# normal/Gaussian
#=============================
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.arange(-3,3,0.001)
#plt.plot(x,norm.pdf(x))
#plt.show()

mu = 5.0
sigma = 2.0
values = np.random.normal(mu,sigma,10000)
#plt.hist(values,50)
#plt.show()
#=================================
#Exponential PDF/'Power law'
#==================================
from scipy.stats import expon
y = np.arange(0,10,0.001)
#plt.plot(y,expon.pdf(y))
#plt.show()

#=======================================
# Binominal Probability mass function
#=====================================
from scipy.stats import binom
#total range and percentage
n,p = 100,0.2
x = np.arange(0,100,0.001)
#plt.plot(x,binom.pmf(x,n,p))
#plt.show()

#=======================================
# Poisson probability mass function
#=========================================
from scipy.stats import poisson

mu = 500
x = np.arange(400,600,0.5)
plt.plot(x,poisson.pmf(x,mu))
plt.show()