'''                        UNIVERSIDAD DE CUENCA        '''
'''Integrantes: 
                Alvarez Andrade Mateo Nicolas
                Guncay Carchipulla Valeria Paola 
                Heredia León Luis Miguel
                Molina Quezada Ana Cristina
    '''
    
'Importacón de librerias'

import matplotlib.pyplot as plt        #Usada para las gráficas 
from scipy.special import factorial2   #Se usa una función especial de scipy ---> factorial2 para el doble factorial 
from matplotlib.widgets import Slider  #Usada para la animación de gráficas 
import numpy as np                     #Necesaria para funciones matemáticas como el seno 
                                       # y transformar de grados a radianes 
                                       
'Variables dependientes e independientes para la función del metronomo'

r = np.arange(40,180,25)
h = 200#longitud de la barra
R= 36.4#distancia masa mayor al eje (mm)
l= 138#longitud barra desde eje hacia arriba
L= h-l#longitud barra desde eje hacia abajo
g = 9800#aceleración gravitacional en mm/s^2
M = 31 #masa mayor gramos
m = 7#masa menor gramos
Mp = M/m
mu = 3.59 #masa de la barra gramos
mup = mu/m
h=L-l #longitud de la barra
theta = 60 #ángulo de oscilacion (grados)

"Función θ"
#Funciónn de angulo-- es una correlación adicional para las grandes oscilaciones entre(40 grados y 60 grados) 
def f_ang(theta):
    """
    Calcula el valor de theta
    
    Parameters
    ----------
    theta : int
        theta es el valor que evalua la función
    Returns
    -------
    int
        Devuelve el ángulo establecido por theta(como argumento).

    """
    return 1+np.sum(np.array([((factorial2(2*n-1)/factorial2(2*n))*(np.sin(np.deg2rad(theta/2)))**(2*n))**2 for n in range(1,151)]))
####################################################################################################################################################
'Modelo de metrónomo ajustado (Ω^2)'
#Transformación y ajuste del modelo
def omega_cuadrado(g,theta,Mp,r,L,mup,l,R,h,m,M,mu):
    """
    Calculo del Omega^2

    Parameters
    ----------
    g : float
    theta : int
    Mp : int
    r : vector
    L : int
    mup : float
    l : int
    R : float
    h : int
    m : int
    M : int
    mu : float

    Returns
    -------
    vector
        Devuelve los valores de omega2

    """
    a_0 = (g/(f_ang(theta))**2)*(Mp*R-(mup/2)*(l-L))/(Mp*(R**2)+(mup/3)*(L**2+l**2-l*L))
    b_2 = -1/(Mp*(R**2)+(mup/3)*(l**2+l**2-l*L))
    return (a_0+(b_2*g/(f_ang(theta))**2)*r)/(1-b_2*r**2)
#Una combinación lineal de términos polinomiales de r
omega2=omega_cuadrado(g = g,theta = 60,Mp=Mp,r=r,L=L,mup=mup, l=138, R=R, h=h, m=m, M=M, mu=mu)

"Gráfica"  
fig, ax = plt.subplots()                        #crea objeto figura
ax.set_ylabel("$\Omega^2$")                     #Título del eje y
ax.set_xlabel('r: Distancia masa al eje (mm)')  #Título del eje x
ax.set_title("Metrónomo de Beethoven")          #Título principal
line, = plt.plot(r,omega2,"-o",label="Control") #Dibujo de la función
plt.subplots_adjust(left=0.25, bottom=0.45)     #Ajustamos el tamaño de la figura (posición del borde izquierdo y posición del borde inferior)
ax.legend(loc='upper right')
plt.show()
                
def update(val):
    """
    Establece las variables a los valores de control deslizante

    Parameters
    ----------
    val : float
        val es el valor del deslizante

    Returns
    -------
    None.

    """
# asignación de los deslizantes
    omega1 = omega_cuadrado(sliderg.val, slidert.val, sliderMp.val , r, sliderL.val, slidermup.val, sliderl.val, sliderR.val, h, m, M, mu) 
    line.set_ydata(omega1)         #actualiza la linea con nuevos datos de omega1
    fig.canvas.draw_idle()         #actualiza la figura que se ha modificado anteriormente
    
axcolor = 'lightgoldenrodyellow'
ax.margins(x=0)  #margen en el eje x

##################################################################################################################################################
"Sliders"
#plt.axes[left, bottom, width, height]
#plt.axes([x,y,largo de la barra,ancho de la barra])
#Slider para longitud barra desde eje hacia arriba 
axl=plt.axes([0.25, 0.35, 0.65, 0.03], facecolor=axcolor) 
sliderl = Slider(axl, 'Longitud barra desde eje hacia arriba', valmin=137, valmax=198,valinit=l)
sliderl.on_changed(update)

#Slider para distancia masa mayor al eje (mm)
axR=plt.axes([0.25, 0.30, 0.65, 0.03], facecolor=axcolor)
sliderR = Slider(axR, 'Distancia de M al eje', valmin=36, valmax=68,valinit=R)
sliderR.on_changed(update)

#Slider para el ángulo Theta
axt=plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
slidert = Slider(axt, 'Theta', valmin=40, valmax=60,valinit=theta)
slidert.on_changed(update)

#Slider para la gravedad (mm/S^2)
axg=plt.axes([0.25, 0.20, 0.65, 0.03], facecolor=axcolor)
sliderg = Slider(axg, 'Gravedad', valmin=9700, valmax=10000,valinit=g)
sliderg.on_changed(update)

#############################################################################################################################################
'Variables dependientes'
# Estas varibles necesitan de las antes mencionadas, debido a que son las resultantes 
# de las operaciones entre estas 

axMp=plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
sliderMp = Slider(axMp, 'Mp', valmin=4.37 , valmax=6 ,valinit=Mp)#aMp depende de dos varibles M y m
sliderMp.on_changed(update)

axL=plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
sliderL = Slider(axL, 'Longitud barra desde eje hacia abajo', valmin=63, valmax=134,valinit=L)#L depende de dos variables h y l
sliderL.on_changed(update)

axmup=plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
slidermup = Slider(axmup, 'mup', valmin=0.5005, valmax=1.5,valinit=mup) #mup dendede de dos varibles mu y m
slidermup.on_changed(update)