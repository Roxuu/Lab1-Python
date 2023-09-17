import numpy as np
import pandas as pd

print('Імпортуємо необхідні бібліотеки')

# 1. Генеруємо випадкові і невипадкові масиви

print('Арифметична прогресія з кроком 2')
a = np.arange(1,16,2)
print(a)

print('Масив з 9 одиниць цілого типу')
b = np.ones(9, dtype=int)
print(b)

print('Двовимірний масив із нулів типу float')
c = np.zeros((2, 4), dtype=float)
print(c)

print('5 рівномірно розподілених чисел від 0 до 1')
d = np.linspace(0, 1, 5)
print(d)

print('Випадкові числа від 0 до 1 розміром 4x3')
e = np.random.random((4, 3))
print(e)

print('Цілі випадкові числа від 0 до 100 розміром 4x4')
f = np.random.randint(0, 100, (4, 4))
print(f)

print('Порожній масив із залишковим вмістом пам\'яті')
g = np.empty(5)
print(g)

# 2. Індексація елементів масиву

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print('Елемент з індексом [1]')
print(a[1])

print('Передостанній елемент')
print(a[-2])

print('Елемент [0, -1]')
print(a[0, -1])

print('Січення з 0 по 1 включно')
print(a[0:2])

print('Січення з кроком 2')
print(a[::2])

print('Зворотний порядок')
print(a[::-1])

# 3. Арифметичні операції

a = np.array([1, 2, 3, 4])

print('Додавання числа до кожного елементу')
print(a + 3)

print('Множення на число')
print(a * 2)

print('Сума всіх елементів')
print(np.add.reduce(a))

print('Накопичення суми елементів')
print(np.add.accumulate(a))

print('Множення елементів з іншим масивом')
print(np.multiply.outer(a, a))

# 4. Обчислення статистики

print('Читання даних')
data = pd.read_csv('iris.csv')

print('Вибірка даних')
petal = np.array(data['petal_width'])

print('Статистичні характеристики')
print(np.min(petal))
print(np.max(petal))
print(np.mean(petal))
print(np.std(petal))
print(np.var(petal))
print(np.median(petal))
print(np.percentile(petal, 25))
print(np.percentile(petal, 75))