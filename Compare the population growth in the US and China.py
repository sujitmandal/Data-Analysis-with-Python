import pandas as pd 
from matplotlib import pyplot as plt 

#This programe is create by Sujit Mandal

data = pd.read_csv('countries.csv')

print(data[data.country == 'United States'])

print('-------------------------------------------')
print('-------------------------------------------')

us = data[data.country == 'United States']
china = data[data.country == 'China']
print(china)
