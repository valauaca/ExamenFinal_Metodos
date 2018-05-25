# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0,2.0,7)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])

## usando central difference 
n=1000
h=x[1]-x[0]

    
derivada=(fx[2:-1]-fx[0:-3])/(2*h)

print (derivada)
    
# segunda derivada
# df(x+h/2)-df(x-h/2)/h*h

segundaderivada= (fx[2:-1] - 2*fx[1:-2] + fx[0:-3])/(h**2)
print (segundaderivada)

    
plt.figure()
plt.plot(x, segundaderivada)
plt.savefig("segunda.png")



