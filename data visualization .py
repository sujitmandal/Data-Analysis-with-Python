import pandas as pd 
from matplotlib import pyplot as plt 

#This programe is create by Sujit Mandal

sample_data = pd.read_csv('sample_data.csv')

print(type(sample_data))
print(sample_data.column_c.iloc[0])