numbers = list(map(float, input("Введіть числа розділені пробілами: ").split()))
average = sum(numbers) / len(numbers)
print(f"Масив чисел: {numbers}")
print(f"Середнє арифметичне: {average}")