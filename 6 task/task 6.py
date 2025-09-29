n = int(input())
results = []

for _ in range(n):
    a, b, x, y = map(int, input().split())

    # Максимальное количество пар для каждого типа контроллера
    # Тип A может работать с любыми модулями
    pairs_A = min(a, x + y)

    # Тип B может работать только с модулями типа 1
    pairs_B = min(b, x)

    # Общее максимальное количество п4ар
    max_pairs = pairs_A + pairs_B

    results.append(max_pairs)

print(results)