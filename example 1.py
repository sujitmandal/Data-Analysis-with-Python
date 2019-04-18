import pandas as pd 
from matplotlib import pyplot as plt 

#This programe is create by Sujit Mandal

x = [1,5,7,9]
y = [2,5,8,6]
z = [5,7,8,10]
plt.plot(x,y)
plt.plot(x,z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y & z")
plt.legend(["this is x","this is y & z"])
plt.show()
