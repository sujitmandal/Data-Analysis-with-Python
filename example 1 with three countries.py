import pandas as pd 
from matplotlib import pyplot as plt 

#This programe is create by Sujit Mandal

data = pd.read_csv('countries.csv')

Algeria = data[data.country == 'Algeria']
Zimbabwe = data[data.country == 'Zimbabwe']
Yemen = data[data.country == 'Yemen, Rep.']

#FOR THREE COUNTRIES:
#FOR NORMAL

data = pd.read_csv('countries.csv')
plt.plot(Algeria.year,Algeria.population)
plt.plot(Zimbabwe.year,Zimbabwe.population)
plt.plot(Yemen.year,Yemen.population)
plt.xlabel("year")
plt.ylabel("population")
plt.legend(["Algeria","Zimbabwec","Yemen"])
plt.show()