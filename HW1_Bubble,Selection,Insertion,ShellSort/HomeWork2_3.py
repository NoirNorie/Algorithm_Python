#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

N_values = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000,
70000, 75000, 80000, 85000, 90000, 95000, 100000, 150000, 200000, 250000, 300000, 350000, 400000,
450000, 500000, 550000, 600000]
shell_values=[0.026, 0.062, 0.090, 0.145, 0.160, 0.213, 0.289, 0.315, 0.371, 0.409, 0.451, 0.494, 0.503,
0.667, 0.693, 0.655, 0.764, 0.934, 0.903, 0.903, 1.488, 2.249, 2.889, 3.657, 4.680, 5.326, 6.175,
7.487, 7.798, 9.119]

plt.plot(N_values, shell_values)

plt.subplot(1,2,2)
plt.plot(N_values, shell_values, color='steelblue')
plt.title('Shell Sorting Trial')

x = [i for i in range(2,10000)]
y = [j * math.log(j,2) for j in range(2,10000)]
plt.subplot(1,2,1)
plt.plot(x,y,color='green')
plt.title('N*logN')
plt.show()


#%%