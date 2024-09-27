import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Requests ->
# r = requests.get('https://yandex.ru/images/')
# query = "Осень"
# # print(r.headers)
# req = requests.get(f'https://www.google.com/search?q={query}&sca_esv=5009c1303de011b0&sca_upv=1&hl=ru&udm=2&biw=1517&bih=674&sxsrf=ADLYWIJsbO7EZXXm6SZoFEhVxe2YeSCKZg%3A1727448167422&ei=Z8T2ZpS1GdnWhbIP9pKPqQo&ved=0ahUKEwjUhIzzreOIAxVZa0EAHXbJI6UQ4dUDCBA&uact=5&oq=autumn&gs_lp=Egxnd3Mtd2l6LXNlcnAiBmF1dHVtbjIQEAAYgAQYsQMYQxiDARiKBTIQEAAYgAQYsQMYQxiDARiKBTILEAAYgAQYsQMYgwEyChAAGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESMsyUKIKWOQwcAp4AJABAZgBigKgAb8QqgEGMC4xNC4xuAEDyAEA-AEBmAIVoAL4DagCCsICBBAjGCfCAgYQABgHGB7CAgQQABgDwgINEAAYgAQYsQMYQxiKBcICCBAAGIAEGLEDwgIJEAAYgAQYARgKwgIHEAAYgAQYCsICCxAAGIAEGAEYGBgKwgIJEAAYgAQYGBgKwgIHECMYJxjqAsICDhAAGIAEGLEDGIMBGIoFwgIEEAAYHpgDDIgGAZIHBjkuMTEuMaAH10Q&sclient=gws-wiz-serp')
# print(req.url) #ссылка на поиск картинок по запросу query, сокротить строку не вышло:(

# Pandas ->
# series = pd.Series([1, 2, 3], index=["a", "b", "c"])
# print(series)
# print(series.index)
# print(series['b'])
# df1 = pd.DataFrame([[1, "Алексей", 1995], [2, "Анна", 1997], [3, "Виталий", 1985]], columns=["№", "Имя", "Год рождения"])
# print(df1)
# df2 = pd.DataFrame([[3, "Георгий", 1996], [4, "Алексей", 1990], [5, "Савелий", 1972]], columns=["№", "Имя", "Год рождения"])
# print(df2)
# print(pd.merge(df1, df2, on='Имя', how="inner"))
# print(pd.merge(df1, df2, on='№', how="inner"))

# Numpy ->
# a = np.array([1, 2, 3])
# a2 = np.array([[1, 2, 3], ['Alex', 'Cat', 'Anna']])
# a3 = np.array([[[1, 2, 3], ['Alex', 'Cat', 'Anna']], [[1995, 2015, 1997], ['Male', 'Animal', 'Female']]])
# # print(a)
# # print(a2)
# # print(a3)
# print(a3.size) # количество элементов 3х мерного массива
# print(a3[0, 1, 1]) # Достать кота
# print(a3[1, 0, :]) # Достать список годов рождения
# a3[0, 1, 1] = "Dog"
# print(a3) # Кот стал собакой
# sevens = np.full((7, 7), 777)
# print(sevens)
# print(a*777) # первый массив умножился на 777
# print((a*777).prod()) # произведение всех элементов предыдущего массива
# print(a>2) # проверка первого массива

# Matplotlib ->
# x = ['Болезни системы кровообращения', 'Новообразования', 'Болезни органов дыхания', 'Внешние причины']
# y = [37, 26, 8.5, 4.6]
# plt.bar(x, y)
# plt.xlabel('Причины') #Подпись для оси х
# plt.ylabel('Процент смертности') #Подпись для оси y
# plt.title('Основные причины смертности населения') #Название
# plt.plot(x, y, color='red', marker='x', markersize=7, alpha=0.5)
# plt.show()

# Pillow ->
filename = "autumn1.png"
with Image.open(filename) as img:
    img.load()
print(img.size)
img.getbands()
cropped_img = img.crop((120, 75, 800, 500)) # кропнутое изображение
# cropped_img.show()

low_res_img = cropped_img.resize((cropped_img.width // 2, cropped_img.height // 2)) # кроп более простым способом
# low_res_img.show()
rotated_img = cropped_img.rotate(45, expand=True) # повернуть на 45% с сохранением углов
gray_img = rotated_img.convert("L")  # ч/б
cmyk_img = rotated_img.convert("CMYK")
# gray_img.show()
low_res_img.save('low_res_img.png')
print(img.getbands())
print(cmyk_img.getbands())
print(gray_img.getbands())

# # red, green, blue = img.split()
red, green, blue, black = cmyk_img.split()
zeroed_band = red.point(lambda _: 0)

red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))


red_merge.show()
green_merge.show()
blue_merge.show()
red_merge.save('red.jpg')
green_merge.save('green.jpg')
blue_merge.save('blue.jpg')
