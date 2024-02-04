import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')  # лимонад
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')  # сік


# Функція цілі (Максимізація кількості)
model += x1 + x2, "Profit"

# Додавання обмежень
model += 2 * x1 + x2 <= 100  # Обмеження для води
model += x1 <= 50  # Обмеження для цукру
model += x1 <= 30  # Обмеження для лим соку
model += 2* x2 <= 40  # Обмеження для фрукт пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти лимонаду:", x1.varValue)
print("Виробляти соку:", x2.varValue)