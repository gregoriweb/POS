import numpy as np
import matplotlib.pyplot as plt


x = np.array([4,3,7,-9,1])
print(x)
print("Tipo:" + str(x.dtype))

print (x.itemsize)
print (x.size)
print (x.itemsize * x.size)
print (x.nbytes)
print (x.ndim)

a=np.arange(15).reshape(3,5)

print(a)
print(a.shape)

print (np.identity(10))
print (np.zeros(10))
print (np.zeros((2,2)))


x=np.linspace(0,2 * np.pi, 100)
f=np.sin(x)
plt.plot(x,f)
plt.show()

x=np.linspace(3, -2, 200)
y= x ** 2 - 2 * x + 1
plt.plot(x,y)
plt.show()