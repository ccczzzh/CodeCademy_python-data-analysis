# Variance is simply the average of the squared differences from the mean.
# Standard Deviation is just the square root of the variance.
import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100,20,10000)
print(incomes)
print(incomes.std())
print(incomes.var())