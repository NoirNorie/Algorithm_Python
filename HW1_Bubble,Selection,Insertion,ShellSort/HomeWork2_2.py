#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

algorithm = ['selection', 'bubble', 'insertion', 'shell']
random_values = [4.079, 11.166, 5.426, 0.055]
sorted_values = [3.563, 5.932, 0.002, 0.014]
reversed_values = [3.919, 17.788, 11.075, 0.029]

def create_x(t,w,n,d):
    return [t*x + w*n for x in range(d)]

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

plt.xlabel('Algorithm with N = 10000')
plt.ylabel('T : Time(/sec)')
plt.title('Comparision of Sorting Algorithm')
plt.show()


#%%