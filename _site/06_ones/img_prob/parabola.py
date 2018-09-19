from matplotlib.pyplot import *
from numpy import *

x = linspace(-50,50)
y = 0.02*x**2
plot(x,y,'-',color='black')
grid()

xticks([-50.0,0.0,50.0], fontsize=20)
yticks([50.0,0.0,50.0], fontsize=20)
xlabel('x (cm)', fontsize=20)
ylabel('Energia potencial (J)', fontsize=20)

show()
