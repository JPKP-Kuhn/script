import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 100)
y = np.cos(t)

plt.plot(t, y)
plt.show()

def plot(func):
    plt.figure(figsize=(12, 8))
    x = np.linspace(-100, 100, 100)
    y = func(x)
    plt.plot(x, y, '-', color='blue')
    plt.show()
    plt.close()


plot(lambda x: x ** 3 - (1 / x))



vd = [5.58, 5.6, 5.61, 5.63, 5.64, 5.65, 5.66, 5.67, 5.67, 5.68]
y = np.arange(5, 51, 5)
y = np.exp(0.1*y)

#Gráfico
plt.title('Gráfico parte 2 Id x Vd')
plt.xlabel('Vd (V)')
plt.ylabel('Id (A)')
#plt.plot(vd, id, 'ro-')
plt.plot(vd, y, 'b-')
plt.grid()
plt.show()