import cv2
import numpy as np

# Загружаем изображение
image = cv2.imread("test2.jpg")

# Создаем окно и показываем оригинальное изображение
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# Добавляем размытие для подавления шума
blurred_image = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)

# Конвертируем в HSV цветовое пространство
hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv_image)
cv2.waitKey(0)

# Устанавливаем границы для ВСЕХ оттенков синего цвета в HSV
# Синий цвет в HSV имеет hue примерно 100-130, но нужно включить светло-синий
hsv_min = np.array((80, 10, 10), np.uint8)  # Нижняя граница синего цвета (включая светло-синий)
hsv_max = np.array((130, 255, 255), np.uint8)  # Верхняя граница синего цвета

# Создаем маску для синих объектов (объединяем два диапазона)
blue_mask = cv2.inRange(hsv_image, hsv_min, hsv_max)
cv2.imshow("Blue Mask", blue_mask)
cv2.waitKey(0)

# Находим контуры синих объектов
contours, hierarchy = cv2.findContours(blue_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Сортируем контуры по площади (от большего к меньшему)
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Создаем копию изображения для рисования
result_image = image.copy()

# Счетчик найденных синих объектов
blue_objects_count = 0

# Минимальная площадь контура для фильтрации шума
min_area = 100

# Обрабатываем каждый найденный синий объект
for i, contour in enumerate(sorted_contours):
    # Проверяем площадь контура
    area = cv2.contourArea(contour)
    if area < min_area:
        continue

    blue_objects_count += 1

    # Получаем координаты ограничивающего прямоугольника
    x, y, w, h = cv2.boundingRect(contour)

    # Вычисляем центр объекта
    center_x = int(x + w / 2)
    center_y = int(y + h / 2)

    # Рисуем красную точку в центре объекта
    cv2.circle(result_image, (center_x, center_y), 8, (0, 0, 255), -1)
    # Показываем финальный результат с точками
    cv2.imshow("Result with Blue Objects", result_image)
    cv2.waitKey(0)