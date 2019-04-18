import pandas as pd 
from matplotlib import pyplot as plt 

#This programe is create by Sujit Mandal

sample_data = pd.read_csv('sample_data.csv')

plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()