import matplotlib.pyplot as plt
import numpy as np
# Alexandro Aguilar NC 0007

cant_productos=[100,150,200,300,500]
precio=[4000,7000,9000,12000,18000]

plt.plot(cant_productos,precio)
plt.show()

# personalizar grafica
plt.plot(cant_productos, precio, color = "red", marker = "o", linestyle = "dashed", linewidth = 2, markersize = 12)
plt.title("Venta de Walmart 0007")
plt.xlabel("Cantidad productos")
plt.ylabel("Precio")
plt.show()

print("Alexandro Aguilar NC 0007")
