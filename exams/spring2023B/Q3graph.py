from numpy import *
import os
from matplotlib import pyplot as plt

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = 'image'
image_dir = os.path.join(current_dir, 'image')
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

k=1.38E-23 #Boltzmann constant in J/K
epsilon=1.6E-19 #Energy in Joules
T = linspace(1, 20000, 10000) #Temperature in K
beta = 1/(k*T) #1/(k*T) in 1/J
power =epsilon*beta
print(power)
num = epsilon*e**(-power)
den = 1 + e**(-power)
E=num/den
delta_T = T[1]-T[0]
C = diff(E)/delta_T
fig2 = plt.figure()
plt.plot(C/k)#(epsilon/k)*T[:-1]
#plt.xscale("log")
plt.xlabel('Temperature')
plt.ylabel('Heat Capacity')
plt.title('Heat Capacity vs Temperature')
plt.show()
image_path = os.path.join(image_dir, 'Q3HeatCapacity.png')
fig2.savefig(image_path)