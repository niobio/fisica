import pylab
from pylab import rc


rc('text', usetex=True)
rc('font', family='serif')
pylab.figure(1, figsize=(6,4))





# Generate data
x = [0,2,4,6,8]
a = [0,5,10,15,20]

# Plot data
#pylab.figure(1)
#pylab.clf()
pylab.plot(x,a,'o-')
pylab.axis([0,9,0,25])

pylab.xlabel(r'{$x$ $\mathrm{(m)}$}')
pylab.ylabel(r'{$a$ $\mathrm{(m/s^2)}$}')
#title(r"\TeX\ is Number $\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
#      fontsize=16, color='r')
pylab.grid(True)
pylab.savefig('fig1.png')


pylab.show()
