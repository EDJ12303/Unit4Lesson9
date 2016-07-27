# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:17:23 2016

@author: Erin
"""
#Generate trials of a normal variable
import random
import numpy as np


mu, sigma = 0, 0.1 # mean and standard deviation
data=np.random.normal(mu, sigma, 1000)

#plot the distribution
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(data, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()

#track the maximum and minimum of each trial of normal variables
    
def trial():
    for i in xrange(100):
        print "max=" 
        print max(data)
        print "min="
        print min(data)
        
trial()
