#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

N_values = [100000, 200000, 300000]

quick_values = [0.291, 0.642, 0.990]
merge_values = [0.763, 1.629, 2.457]
heap_values = [0.865, 1.914, 3.042]

plt.plot(N_values, quick_values)
plt.plot(N_values, merge_values)
plt.plot(N_values, heap_values)

ax = plt.subplot()
ax.set_xticks([100000,200000,300000])

plt.legend(['quick', 'merge', 'heap'])

plt.xlabel('N : Number of Data')
plt.ylabel('T : Time(/sec)')
plt.title('Comparison of Sorting Algorithm')
plt.show()


#%%