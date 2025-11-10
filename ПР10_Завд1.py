import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
y = x ** np.cos(x)

plt.plot(x, y, color='green', linewidth=2, label='Y = x^cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції Y = x^cos(x)')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
