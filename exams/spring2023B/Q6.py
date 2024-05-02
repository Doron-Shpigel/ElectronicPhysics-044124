from sympy.abc import *
from sympy import *
from sympy.vector import CoordSys3D, gradient

C = CoordSys3D('C')

epsilonK = ((h**2)/(2*m))*(C.x**2) + ((h**2)/(2*m))*(C.y**2)

grad_epsilonK = gradient(epsilonK)

print(grad_epsilonK)