import numpy as np
import pylab as plt

fsize = 14 						# font size for plots

def est_exp(x, order):
	'''
	computations of e^x that does not require an x0.  
	''' 						#TODO properly format function definition.
	
	c = np.log2(np.exp(1)) 		# the stored constant 'we have access to'
	y = x*c 					# change of variables for cleanliness.
	dy = y - np.floor(y)
	result = 0.0
	for n in range(order+1): 	# compute terms in taylor series
		result += np.divide( np.divide(dy,c)**n, np.math.factorial(n) ) 
	return result*np.power(2, np.floor(y))
	
order = 5 						# choose the order of your taylor approximation
x_min = 0						# values of x you want to plot
x_max = 10
res = 400 						# linear spacing resolution
x = np.linspace(x_min, x_max, res) 

est = est_exp(x, order) 		# the function can take vectors thanks to numpy
# generate plots
fig, ax = plt.subplots() 		# multiple plots all on figure 'ax'
ax.plot(x,np.abs(np.exp(x)-est)/np.exp(x))
plt.ylabel('\nRelative Error', fontsize=fsize)
plt.xlabel('\nValue of $x$',fontsize=fsize)
plt.show()						# show plot
# plt.savefig('good_approx_plot.png', dpi = 300) # save file

