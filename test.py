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

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()