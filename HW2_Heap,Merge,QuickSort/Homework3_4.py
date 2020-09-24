#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def create_x(t,w,n,d):
    return [t*x + w*n for x in range(d)]

plt.suptitle('Comparision of various quick Algorithm', fontsize=20)

algorithm = ['normal_quick', 'small_quick', 'mid_quick']
random_values = [0.003, 0.002, 0.026]
sorted_values = [0.035, 0.035, 0.024]
reversed_values = [0.040, 0.047, 0.023]

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


algorithm = ['normal_quick', 'small_quick', 'mid_quick']
random_values = [0.005, 0.004, 0.103]
sorted_values = [0.139, 0.142, 0.090]
reversed_values = [0.163, 0.172, 0.085]

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


algorithm = ['normal_quick', 'small_quick', 'mid_quick']
random_values = [0.007, 0.005, 0.219]
sorted_values = [0.303, 0.305, 0.202]
reversed_values = [0.370, 0.364, 0.186]

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