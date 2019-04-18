import pandas as pd 
from matplotlib import pyplot as plt 

#This programe is create by Sujit Mandal

data = pd.read_csv('countries.csv')

data[data.country == 'United States']
us = data[data.country == 'United States']
usa = us.population / us.population.iloc[0] * 100
print(usa)