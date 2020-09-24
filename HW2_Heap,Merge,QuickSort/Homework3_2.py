#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def create_x(t,w,n,d):
    return [t*x + w*n for x in range(d)]

plt.suptitle('Comparision of Sorting Algorithm', fontsize=20)

algorithm = ['quick', 'merge', 'heap']
random_values = [0.002, 0.005, 0.005]
sorted_values = [0.039, 0.006, 0.008]
reversed_values = [0.033, 0.005, 0.005]

value_random_x = create_x(3, 0.8, 1, 3)
value_sorted_x = create_x(3, 0.8, 2, 3)
value_reversed_x = create_x(3, 0.8, 3, 3)

ax = plt.subplot(1,3,1)
ax.bar(value_random_x, random_values)
ax.bar(value_sorted_x, sorted_values)
ax.bar(value_reversed_x, reversed_values)

middle_x = [(a+c)/2 for (a,c) in zip(value_random_x, value_reversed_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(algorithm)

plt.legend(['Random', 'Sorted', 'Reverse'])
plt.xlabel('Algorithm')
plt.ylabel('T : Time(/sec)')
plt.title('N = 1000')


algorithm = ['quick', 'merge', 'heap']
random_values = [0.006, 0.012, 0.016]
sorted_values = [0.141, 0.011, 0.013]
reversed_values = [0.165, 0.010, 0.011]

value_random_x = create_x(3, 0.8, 1, 3)
value_sorted_x = create_x(3, 0.8, 2, 3)
value_reversed_x = create_x(3, 0.8, 3, 3)

ax = plt.subplot(1,3,2)
ax.bar(value_random_x, random_values)
ax.bar(value_sorted_x, sorted_values)
ax.bar(value_reversed_x, reversed_values)

middle_x = [(a+c)/2 for (a,c) in zip(value_random_x, value_reversed_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(algorithm)

plt.legend(['Random', 'Sorted', 'Reverse'])
plt.xlabel('Algorithm')
plt.ylabel('T : Time(/sec)')
plt.title('N = 2000')
plt.plot()


algorithm = ['quick', 'merge', 'heap']
random_values = [0.009, 0.018, 0.019]
sorted_values = [0.308, 0.021, 0.021]
reversed_values = [0.371, 0.020, 0.020]

value_random_x = create_x(3, 0.8, 1, 3)
value_sorted_x = create_x(3, 0.8, 2, 3)
value_reversed_x = create_x(3, 0.8, 3, 3)

ax = plt.subplot(1,3,3)
ax.bar(value_random_x, random_values)
ax.bar(value_sorted_x, sorted_values)
ax.bar(value_reversed_x, reversed_values)

middle_x = [(a+c)/2 for (a,c) in zip(value_random_x, value_reversed_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(algorithm)

plt.legend(['Random', 'Sorted', 'Reverse'])
plt.xlabel('Algorithm')
plt.ylabel('T : Time(/sec)')
plt.title('N = 3000')
plt.plot()

plt.show()

#%%