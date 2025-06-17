import random

def generate_mountain():
    n = int(input())
    mountain = []
    for i in range(n):
        row = [random.randint(1, 100) for _ in range(i + 1)]
        mountain.append(row)
    return mountain
def find_path(mountain):
    n = len(mountain)
    current_row = 0
    current_col = 0
    path = [mountain[0][0]]
    total_time = mountain[0][0]

    for row in range(n - 1):
        left = mountain[row + 1][current_col]
        right = mountain[row + 1][current_col + 1]

        if left <= right:
            current_col = current_col
            path.append(left)
            total_time += left
        else:
            current_col = current_col + 1
            path.append(right)
            total_time += right

    return total_time, path
mountain = generate_mountain()
print("\nСгенерированная гора:")
for row in mountain:
    print(' '.join(map(str, row)))

total_time, path = find_path(mountain)
print("\nМинимальное время спуска: ",total_time)
print("Последовательность участков маршрута:",' '.join(map(str, path)))
