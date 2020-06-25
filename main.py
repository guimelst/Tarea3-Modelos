import numpy as np 
from scipy import stats 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
from fitter import Fitter
import math
from scipy.optimize import curve_fit
from statistics import variance
from scipy.stats import norm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


datos = pd.read_csv('xy.csv')
df=pd.DataFrame(datos)
df.values
datos1 = pd.read_csv('xyp.csv')
df=pd.DataFrame(datos1)



#Parte 1

fX = np.sum(datos.values, axis = 1)#Se encuentra forma de distribución para X
fY = np.sum(datos, axis = 0)#Se encuentra froma de distribución para Y


mux=(df['x']*df['p']).sum()#sacamos mu para x
print ('\u03BCX = ',mux)

muy=(df['y']*df['p']).sum()#sacamos mu para y
print ('\u03BCY = ',muy)

sigmax=np.sqrt((((df['x']**2)*df['p']).sum())-(mux**2)).sum()#encontramos sigma para x
print ('\u03C3X = ',sigmax)

sigmay=np.sqrt((((df['y']**2)*df['p']).sum())-(muy**2)).sum()#encontramos sigma para y
print ('\u03C3Y =',sigmay)

#Parte 3


c1 = df['x'] * df['y'] * df['p']#forma de encontrar la correlacion 
Rxy = c1.sum()#correlación
print('Correlación = ',Rxy)

c2 = (df['x']-mux) * (df['y']-muy) * df['p']##datos de covarianza
Cxy = c2.sum()#resultado de la covarianza
print ('Covarianza = ',Cxy)

Cpearson = (Cxy)/(mux*muy)#coefiente de pearson
print ('Coeficiente de Pearson = ',Cpearson)

#Parte 4

 
ax = np.linspace(5,15,11)

ay = np.linspace(5,25,21)

gx = 1/(np.sqrt(2*np.pi*sigmax**2))*np.exp(-(ax-mux)**2/(2*sigmax**2))
gy = 1/(np.sqrt(2*np.pi*sigmay**2))*np.exp(-(ay-muy)**2/(2*sigmay**2))
plt.plot(ax,gx)
plt.savefig('Función de densidad marginal X')
plt.plot(ay,gy)
plt.savefig('Función de densidad marginal Y')



#(0.02683* np.exp(-0.0636981*((ax-9.93536)**2)-0.0177*ay**2))



x, y = np.meshgrid(ax,ay)

fxy= (1/(2*np.pi*3.29944287*6.02693775))*np.exp(-(((x-9.90484381)**2)/(2*3.29944287**2) + ((y-15.0794609)**2)/(2*6.02693775**2)))

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, fxy)
plt.xlabel('Valor de x')
plt.ylabel('Valor de y')
ax.set_title('Función Densidad conjunta')
plt.savefig('Función Densidad conjunta xy')
plt.show()

