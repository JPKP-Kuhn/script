#%%
from curses.ascii import isspace
import matplotlib.pyplot as plt
import numpy as np

#Pontos do gráfico
id = [5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0]
vd = [5.58, 5.6, 5.61, 5.63, 5.64, 5.65, 5.66, 5.67, 5.67, 5.68]


def plot(func):#Gráfico
    plt.title('Gráfico parte 2 Id x Vd')
    plt.xlabel('Vd (V)')
    plt.ylabel('Id (mA)')
    x = np.arange(5.55, 5.7, 0.01)
    y = func(x)
    plt.plot( vd, id, 'ro-')
    #plt.plot(x, y, '-', color='blue')
    plt.grid()
    plt.show()
    plt.close()
    
plot(lambda x: x ** 3 - (1 / x))#Chamada da função plot
