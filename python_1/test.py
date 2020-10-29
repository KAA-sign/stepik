# from numpy import *

from pylab import *

# a = array([2, 3, 4])
# print(a)

# b = array([(1.5, 2, 3), (4, 5, 6)])
# print(b)

# z = zeros((3, 2))
# print(z)

x = linspace(0, 5, 10)
y = x ** 2
print(x)
print(y)

# figure()
# plot(x, y, 'r')
# xlabel('x')
# ylabel('y')
# title('title')
# show()

# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

# axes1.plot(x, y, 'r')
# axes1.set_xlabel('x')
# axes1.set_ylabel('y')
# axes1.set_title('title')

# axes2.plot(y, x, 'g')
# axes2.set_xlabel('y')
# axes2.set_ylabel('x')
# axes2.set_title('insert title')

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
    
fig.tight_layout()