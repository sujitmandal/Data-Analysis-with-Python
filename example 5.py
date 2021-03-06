import pandas as pd 
from matplotlib import pyplot as plt 

#This programe is create by Sujit Mandal

data = pd.read_csv('countries.csv')

Algeria = data[data.country == 'Algeria']
Zimbabwe = data[data.country == 'Zimbabwe']

#FOR PERCENTAGE(%):

plt.plot(Algeria.year,Algeria.population / Algeria.population.iloc[0] * 100)
plt.plot(Zimbabwe.year,Zimbabwe.population / Zimbabwe.population.iloc[0] * 100)
plt.xlabel("year")
plt.ylabel("population groth (first year = 100)")
plt.legend(["Algeria","Zimbabwec"])
plt.show()