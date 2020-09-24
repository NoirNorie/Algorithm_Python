#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def create_x(t,w,n,d):
    return [t*x + w*n for x in range(d)]

plt.suptitle('Comparision of Algorithm', fontsize=20)

algorithm = ['cocktail', 'exchange', 'bubble', 'selection']
random_values = [2.636, 1.648, 2.732, 0.985]
sorted_values = [1.182, 2.610, 1.252, 0.882]
reversed_values = [3.985, 0.896, 4.001, 0.992]

value_random_x = create_x(3, 0.8, 1, 4)
value_sorted_x = create_x(3, 0.8, 2, 4)
value_reversed_x = create_x(3, 0.8, 3, 4)

ax = plt.subplot()
ax.bar(value_random_x, random_values)
ax.bar(value_sorted_x, sorted_values)
ax.bar(value_reversed_x, reversed_values)

middle_x = [(a+c)/2 for (a,c) in zip(value_random_x, value_reversed_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(algorithm)

plt.legend(['Random', 'Sorted', 'Reverse'])
plt.xlabel('Algorithm')
plt.ylabel('T : Time(/sec)')
plt.title('N = 5000')

plt.show()
#%%