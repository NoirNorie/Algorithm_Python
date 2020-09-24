#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

N_values = [5000, 10000, 15000]

selection_values = [0.998, 3.958, 9.002]
bubble_values = [2.655, 10.511, 23.609]
insertion_values = [1.373, 5.413, 12.006]
shell_values = [0.025, 0.050, 0.087]

plt.plot(N_values, selection_values)
plt.plot(N_values, bubble_values)
plt.plot(N_values, insertion_values)
plt.plot(N_values, shell_values)

ax = plt.subplot()
ax.set_xticks([5000,10000,15000])

plt.legend(['selection', 'bubble', 'insertion', 'shell'])

plt.xlabel('N : Number of Data')
plt.ylabel('T : Time(/sec)')
plt.title('Comparison of Sorting Algorithm')
plt.show()


#%%