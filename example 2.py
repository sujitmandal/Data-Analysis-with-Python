import pandas as pd 
from matplotlib import pyplot as plt 

#This programe is create by Sujit Mandal

sample_data = pd.read_csv('sample_data.csv')

plt.plot(sample_data.column_a,sample_data.column_b)
plt.plot(sample_data.column_a,sample_data.column_c)
plt.xlabel("column_a")
plt.ylabel("column_b & column_c")
plt.legend(["this is column_a","this is column_a & column_c"])
plt.show()
