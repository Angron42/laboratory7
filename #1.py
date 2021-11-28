from numpy import sin, cos, linspace
import matplotlib.pyplot as plt

x = linspace(1, 10, 51)
y = 5 * sin(x) * (cos(x**2 + 1/x) ** 2)

plt.plot(x, y, 'ro-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Функция под номером 20')
plt.savefig('graph_1.png', dpi=200)
plt.show()
