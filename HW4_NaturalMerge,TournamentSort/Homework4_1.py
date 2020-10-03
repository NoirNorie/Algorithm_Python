#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def create_x(t,w,n,d):
    return [t*x + w*n for x in range(d)]

plt.suptitle('Comparision of various quick Algorithm', fontsize=20)

algorithm = ['natural', 'merge']
random_values = [0.070, 0.005]
sorted_values = [0.000, 0.005]
reversed_values = [0.051, 0.005]

value_random_x = create_x(3, 0.8, 1, 2)
value_sorted_x = create_x(3, 0.8, 2, 2)
value_reversed_x = create_x(3, 0.8, 3, 2)

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


algorithm = ['natural', 'merge']
random_values = [0.245, 0.010]
sorted_values = [0.001, 0.012]
reversed_values = [0.185, 0.014]

value_random_x = create_x(3, 0.8, 1, 2)
value_sorted_x = create_x(3, 0.8, 2, 2)
value_reversed_x = create_x(3, 0.8, 3, 2)

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


algorithm = ['natural', 'merge']
random_values = [0.518, 0.019]
sorted_values = [0.001, 0.019]
reversed_values = [0.402, 0.018]

value_random_x = create_x(3, 0.8, 1, 2)
value_sorted_x = create_x(3, 0.8, 2, 2)
value_reversed_x = create_x(3, 0.8, 3, 2)

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