#!/usr/local/bin/python
from math import *
import matplotlib.pyplot as plt
import os
import errno

## heatEq.py
## Remi Carmigniani
## Solves the 1D heat equation :
## pd_t u[x,t] - pd_xx u[x,t] = 0 x in 0 1
## BC u[0,t] = 0 and u[1,t] = 1
## IC u[x,0]=x +sin (pi *x) 

##

directory='result'
if not os.path.exists(directory):
    os.makedirs(directory)
## Discretization parameter 
N=25
L=1
dx=L/float(N-1)
dt = .25*dx**2 
t=0
tend = 1./(2.*pi)
l = dt/dx/dx

#plot axis
x1 = 0
x2 = 1
y1 = 0
y2 = 1.6


#dt is such that dt/dx^2 < 0.5 
s = 'The resolution is ' + repr(dx) + ', and the time step is ' + repr(dt) 
print s

## generate the initial conditions

## Initial positions
def iCond(x):
    return x + sin(pi*x)

uval = iCond(0)
u_arr = [uval]
x_arr = [0]

for i in range(1,N):
    uval = iCond(i*dx)
    x_arr.append(i*dx)
    u_arr.append(uval)
    
#plot the initial data
numb = 0
plt.plot(x_arr, u_arr)
plt.ylabel('U')
plt.xlabel('x')
plt.title('t = '+ repr(t)) 
plt.axis([x1, x2, y1, y2])
plt.savefig(directory +'/t'+'%0*d' % (3, numb)+'.png')

step=0
stepSize = int(tend/dt/10)
s = 'The number of time step is  : ' + repr(stepSize)
print s
#Time loop
while t<=tend :
	t=t+dt
	uold = u_arr[:]
	for i in range(1,N-1):
		u_arr[i] = l*uold[i-1]+(1-2.*l)*uold[i]+l*uold[i+1]
        step=step+1
        if step%stepSize == 0:
        	step = 0
        	numb = numb+1
        	plt.clf()
        	plt.plot(x_arr, u_arr)
		plt.ylabel('U')
		plt.xlabel('x')
		plt.title('t = '+ repr(t))
		plt.axis([x1, x2, y1, y2]) 
		plt.savefig(directory +'/t'+'%0*d' % (3, numb)+'.png')
		
        	

       
	
	


