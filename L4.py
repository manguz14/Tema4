# Base para la solución del Laboratorio 4

# Los parámetros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Variables aleatorias A y Z
vaX=  stats.norm(0, np.sqrt(5))
vaY = stats.norm(0, np.sqrt(5))

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 10
W = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t) (A y Z independientes)

for i in range(N):   
   X = vaX.rvs()        
   Y = vaY.rvs()     
   w = X*np.cos(np.pi*t) + Y*np.sin(np.pi*t) 
   W[i,:] = w
   plt.plot(t, w)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(W[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6)

# Graficar el resultado teórico del valor esperado

E = 0*t
plt.plot(t, E, '-.', lw=4)

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.show()

# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr =  np.empty((N, len(desplazamiento)))
media = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación
plt.figure()

# Cálculo de correlación para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(W[n,:], np.roll(W[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de correlación
Rww = 25*np.cos(np.pi*taus)

# Gráficas de correlación para cada realización 
plt.plot(taus, Rww, '-.', lw=4, label='Correlación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend()
plt.show()



# Gráficas de para la media
plt.plot(taus, E, '-.', lw=4, label='Media')
plt.title('Media de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$E_{X}(\tau)$')
plt.legend()
plt.show()








