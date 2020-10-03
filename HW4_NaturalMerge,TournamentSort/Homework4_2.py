#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

N_values = [1000, 2000, 3000]

random_values = [0.453, 1.828, 5.563]
sorted_values = [0.451, 1.818, 5.162]
reversed_values = [0.410, 1.647, 4.933]

plt.plot(N_values, random_values)
plt.plot(N_values,sorted_values)
plt.plot(N_values, reversed_values)

ax = plt.subplot()
ax.set_xticks([1000,2000,3000])

plt.legend(['random','sorted','reversed'])

plt.xlabel('N : Number of Data')
plt.ylabel('T : Time(/sec)')
plt.title('Comparison of Sorting Algorithm')
plt.show()


#%%