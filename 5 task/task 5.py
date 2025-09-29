# Читаем размеры матрицы
h, w = map(int, input().split())

# Читаем матрицу
matrix = []
for i in range(h):
    row = list(map(int, input().split()))
    matrix.append(row)

# Находим координаты всех единиц
ones_coords = []
for i in range(h):
    for j in range(w):
        if matrix[i][j] == 1:
            ones_coords.append((i, j))
            print('Координаты единиц: ',i,j)

# Находим минимальные и максимальные координаты фигуры
min_row = min(coord[0] for coord in ones_coords)
max_row = max(coord[0] for coord in ones_coords)
min_col = min(coord[1] for coord in ones_coords)
max_col = max(coord[1] for coord in ones_coords)
print(min_row,
max_row,
min_col,
max_col)

# Координаты ограничивающего прямоугольника (с отступом в 1 единицу)
top_left_row = min_row - 1
top_left_col = min_col - 1
bottom_right_row = max_row + 1
bottom_right_col = max_col + 1

# Выводим координаты
print(top_left_row, top_left_col, bottom_right_row, bottom_right_col)