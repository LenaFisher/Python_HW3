# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]

def f(list):
    list2 = []
    for i in range((len(list)+1)//2):
        list2.append(list[i]*list[len(list)-1-i])
    return list2

print(f(list))



