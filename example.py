from xfoil import XFoil
import matplotlib.pyplot as plt
xf = XFoil()

xf.load("clarky.dat")
plt.plot(xf.airfoil.x,xf.airfoil.y)
plt.axis('equal')
plt.show()


