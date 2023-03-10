# Списки
## Создание списка

list_1 = []        # Создание пустого списка
list_1 = list()    # Создание пустого списка - функция 
print(list_1)      # Ответ []

list_1 = [1, 2, 3, 8]
print(list_1)      # Ответ [1, 2, 3, 8]

print(*list_1)     # * уберем скобочки, запятые. Ответ 1 2 3 8

for i in list_1:
    print(i)

print(len(list_1)) # количество элементов в списке. Ответ 4

print(list_1[0])   # обращаемся к элементу Ответ 1
print(list_1[-1])  # индексация с конца

## Добавление в список

list_1 = [1, 5]
print(list_1) 
list_1.append(8)  # добавление элемента в конец список
print(list_1)     # Ответ [1, 5, 8]
list_1.append(85)
print(list_1)     # Ответ [1, 5, 8, 85]


list_1 = []
print(list_1) 
for i in range(5):  # Дополняем список значениями
    list_1.append(i)
    print(list_1) 
# []   Ответ
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]
