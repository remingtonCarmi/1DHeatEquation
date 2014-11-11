Solve the 1D heat equation
u_t-u_xx = 0 for x in 0  1
u(x=0,t) = 0
u(x=1,t) = 1
u(x,  0) = x + sin(pi*x)

Depenencies: 
 matplotlib.pyplot as plt (for plotting)

***********************************************************************

Solver use a center schemes for the space differenciation and explicit euler for the time
to be stable require :  dt/dx*dx <0.5

save the plot in result
to convert in gif use the command : 
 convert result/*png 1DHeatEquation.gif
