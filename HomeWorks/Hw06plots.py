from sympy import *
from sympy.abc import *
from numpy import *
import matplotlib.pyplot as plt

# Define the constants
tau = 8e-15
sigma = 4e7
omega = linspace(0,1e15,1000)

# Define the functions

RealOmega = sigma/(1+omega**2*tau**2)
ImagOmega = sigma*tau*omega/(1+omega**2*tau**2)
AbsOmega = sigma*sqrt(1+omega**2*tau**2)/(1+omega**2*tau**2)

# Plot the functions, label in latex
fig, ax = plt.subplots()
plt.plot(omega, RealOmega, label=r'$\Re\{\omega\}$')
plt.plot(omega, ImagOmega, label=r'$\Im\{\omega\}$')
plt.plot(omega, AbsOmega, label=r'$\Vert\sigma_{AC}\omega\Vert$')
plt.xlabel(r'$\omega [rad/s]$')
plt.ylabel('Magnitude')
plt.legend()
# Remove unnecessary white space
ax.autoscale()
ax.margins(0)  # Set margins to zero
plt.tight_layout()

plt.show()

