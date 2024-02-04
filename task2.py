import scipy.integrate as spi
import numpy as np

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
def f(x):
    return x**3
# Визначте межі інтегрування, наприклад, від 0 до 1
a = 0  # нижня межа
b = 2  # верхня межа

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл (quad): ", result)

def monte_carlo_integrate(func, a, b , num_points):
    y_min = func(a)
    y_max = func(b)
    x = np.random.uniform(a, b , num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = sum(y < func(x))
    area = (b-a) * (func(b)) * (under_curve/ num_points)
    return area

for _ in range(5):
    mk_result= monte_carlo_integrate(f, a, b, 10_000_000)
    print("Інтеграл (monte-karlo): ", mk_result)