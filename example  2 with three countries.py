import pandas as pd 
from matplotlib import pyplot as plt 

#This programe is create by Sujit Mandal

data = pd.read_csv('countries.csv')

Algeria = data[data.country == 'Algeria']
Zimbabwe = data[data.country == 'Zimbabwe']
Yemen = data[data.country == 'Yemen, Rep.']

#FOR THREE COUNTRIES:
#FOR MILION(10^6=1,000,0000):

data = pd.read_csv('countries.csv')
plt.plot(Algeria.year,Algeria.population / 10**6)
plt.plot(Zimbabwe.year,Zimbabwe.population / 10**6)
plt.plot(Yemen.year,Yemen.population / 10**6)
plt.xlabel("year")
plt.ylabel("population")
plt.legend(["Algeria","Zimbabwec","Yemen"])
plt.show()