import matplotlib.pyplot as plt
import numpy as np
# Alexandro Aguilar NC 0007

cant_productos=[100,150,200,300,500]
precio=[4000,7000,9000,12000,18000]

plt.plot(cant_productos,precio)
plt.show()

# presonalizar grafica
plt.plot(cant_productos, precio,color="green",marker="o")
plt.title("ventas de walmart 0007")
plt.xlabel("cant prod")
plt.ylabel("precio")