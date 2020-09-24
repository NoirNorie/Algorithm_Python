#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

N_values = [100000, 200000, 300000]

quick_values = [0.294, 0.670, 1.061]
quick_small_values = [0.243, 0.551, 0.874]

plt.plot(N_values, quick_values, '-o')
plt.plot(N_values, quick_small_values, '-o')

ax = plt.subplot()
ax.set_xticks([100000,200000,300000])

plt.legend(['normal', 'small'])

plt.xlabel('N : Number of Data')
plt.ylabel('T : Time(/sec)')
plt.title('Comparison of Sorting Algorithm')
plt.show()


#%%