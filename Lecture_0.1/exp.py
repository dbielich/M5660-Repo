import numpy as np
import pylab as plt

fsize = 14
def est_exp(x, x0, order):
	result = 0.0
	y = x - x0
	for n in range(order):
		result += np.divide(y**n,np.math.factorial(n) )
	return result*np.exp(x0)
order = 9
x0 = 152
# x = np.linspace(x0-0.5,x0+0.5,20)
x = np.linspace(x0-5,x0+5,20)
est = est_exp(x, x0, order)
fig, ax = plt.subplots() #multiple plots all on figure ax
ax.plot(x,np.abs(np.exp(x)-est)/np.exp(x))
plt.ylabel('\nRelative Error', fontsize=fsize)
plt.xlabel('\nValue of $x$ near $x_0$',fontsize=fsize)
plt.axvline(x0,color='r',linestyle='--') # vertical line
plt.show()

