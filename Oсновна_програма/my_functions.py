# Основна програма

from my_functions import calculate_expression

# Введення значень x та y від користувача
x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))

# Виклик функції calculate_expression з модуля my_functions
result = calculate_expression(x, y)
print(f"Результат обчислення z = {result}")
