# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 



import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



plt.figure()
plt.plot(x,y)
plt.show()
plt.savefig(xy.png)

plt.image()
plt.plot(x,z)
plt.show()
plt.savefig(xz.png)



