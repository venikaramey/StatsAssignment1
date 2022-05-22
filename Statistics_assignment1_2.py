import numpy as np
import scipy as stats
import math
import statistics
import os
import sys
from scipy import integrate
import pandas as pd
import scipy.special
from scipy.stats import binom
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats import poisson
# Problem statement 7
#We need to calculate average number of customers arriving per 4 minutes
#72/60 customers come per minute
mu = 4*(72/60) #customers come per 4 minutes
# print(f"The probability of arriving 5 cutomers in 4 minutes is : {poisson.pmf(k=5,mu=mu)}")
# print(f"The probability of arriving not more than 3 customers in 4 minutes is : {poisson.pmf(k=3, mu=mu)}")
# print(f'The Probability of more than 3 customers arriving in 4 minutes is : {1-poisson.cdf(k=3,mu=mu)}')

x = list(range(0,10))
fig,ax = plt.subplots(1,1,figsize=(15,5))
ax.plot(x, poisson.pmf(x,mu), 'bo', ms=8, label='poisson pmf')
ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)
plt.xlabel('Number of customers')
plt.ylabel('Probability')
# plt.show()

# Problem statement 8
#Rate of entering=77 per minute
#error rate= 6/hour=0.1 per minute
#No of errors per word=0.1/77
unit_mu=0.1/77
def mu(n):
    return n * unit_mu
# print(f"The pobability of commiting 2 errors in 455 words financial report is :{poisson.pmf(2,mu=mu(455))}")
# print(f"The pobability of commiting 2 errors in 1000 words financial report is :{poisson.pmf(2,mu=mu(1000))}")
# print(f"The pobability of commiting 2 errors in 255 words financial report is :{poisson.pmf(2,mu=mu(255))}")
x=range(100,1000,50)
mu=[i*unit_mu for i in x]
fig,ax = plt.subplots(1,1,figsize=(15,5))
ax.plot(x,poisson.pmf(2,mu), 'bo', ms=8, label='poisson pmf')
ax.vlines(x,0, poisson.pmf(2,mu), colors='b', lw=5, alpha=0.5)
###As the number of words increase probability of getting errors increases

fig,ax = plt.subplots(1,1,figsize=(15,5))
ax.plot(x,mu, 'bo', ms=8, label='poisson pmf')
ax.vlines(x,0,mu, colors='b', lw=5, alpha=0.5)
# plt.show()
####Value of mu keeps on increasing with number of words

# Problem statement 9 is same as Problem 4

# Problem statement 10
def P(z,b=-np.inf) :
    return integrate.quad(norm.pdf,b,z)[0]

# print('P(Z>1.26) = %.5f'%(1-P(1.26)))
# print('P(Z<-0.86) = %.5f'%P(-0.86))
# print('P(Z>-1.37) = %.5f'%(1-P(-1.37)))
# print('P(−1.25 < Z < 0.37) = %.5f'%P(0.37,b=-1.25))
# print('P(Z ≤ −4.6) = %.5f'%P(-4.6))
# print('P(Z>z)=0.05 is %.2f'%(-1*norm.ppf(0.05)))
# print('𝑃(−𝑧 < 𝑍 < 𝑧) = 0.99 is %.2f'%(abs(norm.ppf(0.005))))

# Problem statement 11
mean = 10
std = np.sqrt(4)

def I(z, b=-np.inf):
    z = (z-mean)/std
    return integrate.quad(norm.pdf,b,z)[0]
# print("Probability that current > 13mA is: {}".format(1-I(13)))
# print("Probability that current is between 9 mA and 11 mA is : {}".format(1-I(11,b=9)))

# Problem statement 12

mean_dia=0.2508
std_dia=0.0005
##specified dia in the range of 0.2485<d<0.2515
##case-1 if mean_dia=0.2508
def I(mean,std,a,b) :
  #gives P(Z<=x)
  a=(a-mean)/std
  b=(b-mean)/std
  return a,b
# print(f"Proportion of shafts with dia in range of 0.2485<d<0.2515 when mean diameter:{0.2508,I(0.2508,0.0005,0.2485,0.2515)}")
# print(f"Proportion of shafts with dia in range of 0.2485<d<0.2515 when mean diameter:{0.2500,I(0.2500,0.0005,0.2485,0.2515)}")

##Within the range of 0.2485<d<0.2515 A manufacturing process with mean of 0.25 gives maximum proportion of required shafts, there by reducing amount of scrap and reprocessing time.
##When compared to any other manufacturing process whose mean deviates from that of 0.25 less proportion of required shafts are obtained. The more the manufucaturing process deviaties from 0.25, lesser will be the proportion of reqired shafts obtained.
##Mathematically, in a given range 0.2485<d<0.2515 , if there are two noraml distributrions (manufacturing processes) with same standard deviation,more area will be covered by the distribution whose mean is closer to mean of the interval i.e 0.25