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
import matplotlib.pyplot as plt

# Problem statement 1
marks =np.asarray([6,7,5,7,7,8,7,6,9,7,4,10,6,8,8,9,5,6,4,8])
# print("the mean marks are {}".format(np.mean(marks)))
# print("the median marks are {}".format(np.median(marks)))
# print("the mode marks are {}".format(statistics.mode(marks)))
# print("the std. daviations marks are {}".format(np.std(marks)))
#Problem statement 2
calls = np.asarray([28, 122, 217, 130, 120, 86, 80, 90, 140, 120, 70, 40, 145, 113, 90, 68, 174, 194, 170,100, 75, 104, 97, 75,123, 100, 75, 104, 97, 75, 123, 100, 89, 120, 109])
# print("the mean marks are {}".format(np.mean(calls)))
# print("the median marks are {}".format(np.median(calls)))
# print("the mode marks are {}".format(statistics.mode(calls)))
# print("the std. daviations marks are {}".format(np.std(calls)))
#Problem statement 3
x = np.asarray([0,1,2,3,4,5])
f_x = np.array([0.09,0.15,0.40,0.25,0.10,0.01])
mean=np.dot(x,f_x)
variance_of_x=(x-mean)**2
variance = np.dot(variance_of_x,f_x)
# print("mean number of workoutsis {}".format(mean))
# print("Variance of workouts is {}".format(variance))
#Problem statement 4
PDF=lambda d:20*(np.exp((-20*(d-12.5))))
x = 12.6
P_x=integrate.quad(PDF,12.6,np.inf)
y = 11
CDF=integrate.quad(PDF,-np.inf,y)
# print(f"Proportion of Parts need to scrapped when d >12.6mm is :{P_x[0]}")
# print(f"CDF when d= 11mm is:{CDF[0]}")
# print(f"Proportion of CDF when d>12.5mm is : {integrate.quad(PDF,12.5,np.inf)[0]}")
#Conclusion
#it can be concluded that the function is only valid when d>=12.5.
#When d<12.5, the part can be reworked to 12.5 so no scrap in this case.
#PDF is not defined for d=11

#Problem statement 5
#x = faulty = 0.3
#y = not faulty = 0.7
x = 0.3
y = 0.7
df=pd.DataFrame({'a':[int(i) for i in range(7)],
                 'B_a':[scipy.special.comb(6,i)*(x**i)*(y**(6-i)) for i in range(7)]})
df['Expected value']=df['a']*df['B_a']
mean=np.round(df['Expected value'].sum())
# print('mean = {}'.format(mean))
df['variance']=df['B_a']*(df['a']-mean)**2
std=np.sqrt(df['variance'].sum())
# print(f"Standard Deviation : {np.round(std)}")

#Problem statement 6
# print(f"Probability of each of them solving 5 questions correctly is:{binom.pmf(5,8,0.75)*binom.pmf(5,12,0.45)}")
# print(f"Probability of each of them solving 4,6 questions correctly is:{binom.pmf(4,8,0.75)*binom.pmf(6,12,0.45)}")
# #their correction rates effect their combined probability
# #following graphs show their correction rates invidually and combined
def binom_plot(n,p,):
    fig,ax=plt.subplots(1,1)
    x = np.arange(binom.ppf(0.01, n, p),binom.ppf(0.99, n, p))
    ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
    ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)

#Gaurav
binom_plot(8,0.75)
#Barakha
binom_plot(12,0.45)
#Combined
fig,ax=plt.subplots(1,1)
x = np.arange(1,11)
ax.plot(x, binom.pmf(x,8,0.75)*binom.pmf(x,12,0.45), 'bo', ms=8, label='binom pmf')
ax.vlines(x, 0, binom.pmf(x,8,0.75)*binom.pmf(x,12,0.45), colors='b', lw=5, alpha=0.5)
## maximum combined probability observed at 6 question
plt.show()



