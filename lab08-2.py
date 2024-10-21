import random as r
M = int(input("Введіть кількість рядків (M): "))
N = int(input("Введіть кількість стовпців (N): "))
limit = M*N
array = [[r.randint(1, 20) for _ in range(N)] for _ in range(M)]
print("Масив:")
for row in array:
    row_sum = sum(row)
    if row_sum <= limit:
        print(row)
    else:
        print(f"Сума елементів рядка {row_sum} перевищує ліміт {limit}")