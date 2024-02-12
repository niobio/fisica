from matplotlib.pyplot import *
x=[0,0.18,0.36,0.54]
y=[0,0.25,0.50,0.75]
plot(x,y,'*-',color='black',markersize=12)
grid()
xticks([0.0,0.18,0.36,0.54,0.72,0.90])
yticks([0.0,0.25,0.50,0.75,1.00])
xlabel('sin(r)')
ylabel('sin(i)')
show()
