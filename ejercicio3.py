#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Grafique las dos series de datos en una misma imagen 'serie.png'
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])


plt.figure()
a=plt.plot(t,u, c="k")
b=plt.plot(t,v, c="b")
plt.show()
plt.savefig("serie.png")


# para la covarianza se usa la formula
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

# primero hallar la matriz de covarianza

a=len(u)
b=len(v)

covar=np.zeros((a,b))
def matriz(u, v):
	# for para recorrer la matriz, el rango es la longitud de la fila (cuantas variables tengo)
    mediai=np.mean(u)
    mediaj=np.mean(v)
    for i in range (a):
        for j in range (b):
            n=b
            covar[i,j]=np.sum((u-mediai)*(v-mediaj))/(n-1.0)	
    print (covar)

matriz(u,v)