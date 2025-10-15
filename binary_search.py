def binary_search(lst, item):
    low = 0 # нижняя граница списка (left = 0)
    high = len(lst) - 1 # верхняя граница списка (right = len(list) - 1)

    while low <= high:
        mid = (low + high) // 2 # берем середину списка
        guess = lst[mid] # Индекс среднего числа
        if guess == item: # если элемент найден, возвращаем его индекс
            return mid

        if guess > item:
            high = mid - 1 # отсекаем правую часть списка
        else:
            low = mid + 1 # отсекаем левую часть списка
    return -1 # если вышли из цикла — элемент не найден


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
item = 4

result = binary_search(my_list, item)

if result != -1:
    print("Found at index: ", result)
else:
    print('Not found')
