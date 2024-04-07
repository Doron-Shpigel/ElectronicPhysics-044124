from numpy import *
import os
# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = 'image'
image_dir = os.path.join(current_dir, 'image')
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

k=1.38E-23 #Boltzmann constant in J/K
epsilon=1.6E-19 #Energy in Joules
T = linspace(0.1, 2000, 200000) #Temperature in K
beta = 1/(k*T) #1/(k*T) in 1/J
BE =beta*k
print(e**(BE))
num = epsilon*e**(-BE)+50*epsilon*e**(-50*BE)
den = 1+e**(-BE)+e**(-50*BE)
E=num/den
from matplotlib import pyplot as plt
fig1 = plt.figure()
ax = plt.gca()
plt.plot(T, E)
plt.xlabel('Temperature (K)')
plt.ylabel('Energy (J)')
plt.title('Energy vs Temperature')
e2 = epsilon/2
plt.plot(T, e2*ones(len(T)))
epsilon17 = 17*epsilon
plt.plot(T, epsilon17*ones(len(T)))
plt.legend(['E', 'epsilon/2', '17*epsilon'])
plt.xscale("log")   
ax.set_ylim([0, 17*epsilon])
plt.yticks([0, epsilon/2, 17.5*epsilon], ['0', 'epsilon/2', '17epsilon'])
plt.show()
image_path = os.path.join(image_dir, 'Q3energy.png')
fig1.savefig(image_path)

delta_T = T[1]-T[0]
C = diff(E)/delta_T
print(C)
fig2 = plt.figure()
plt.plot(T[:-1], C)
plt.xscale("log")
plt.xlabel('Temperature (K)')
plt.ylabel('Heat Capacity (J/K)')
plt.title('Heat Capacity vs Temperature')
plt.show()
image_path = os.path.join(image_dir, 'Q3HeatCapacity.png')
fig2.savefig(image_path)

