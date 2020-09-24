#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

N_values = [5000, 10000, 15000]

cs_values = [2.636, 10.432, 23.655]
ex_values = [1.648, 6.655, 14.963]
selection_values = [0.985, 3.891, 8.812]
bubble_values = [2.732, 10.710, 23.138]

plt.plot(N_values, cs_values)
plt.plot(N_values, ex_values)
plt.plot(N_values, selection_values)
plt.plot(N_values, bubble_values)

ax = plt.subplot()
ax.set_xticks([5000, 10000, 15000])

plt.legend(['cocktail', 'exchange', 'selection', 'bubble'])

plt.xlabel('N : Number of Data')
plt.ylabel('T : Time(/sec)')
plt.title('Comparison of Sorting Algorithm')
plt.show()


#%%