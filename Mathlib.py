from numpy import*
from math import*
import matplotlib.pyplot as plt

x = linspace(-3,3,50)
y =pow(2,x)*sin(10*x)

plt.plot(x,y,'g--', label = '')
plt.savefig('y.png', dpi = 200)
plt.axis([-3,3,-1,1])
plt.xlabel('x')
ply.ylabel('y')

plt.title('My first normal plot')
plt.legend()

plt.show()
