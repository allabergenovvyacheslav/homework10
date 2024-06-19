def get_matrix(n, m, value):  # Объявите функцию
    matrix = []              # создаем пустой список matrix
    for i in range(n):       # внешний цикл для кол-ва строк, n повторов
        get = []             # добавляем пустой список для строки n
        for j in range(m):   # внутренний цикл для кол-ва столбцов, m повторов.
            get.append(value)  # строку пополняем значением value
        matrix.append(get)    # матрицу пополняем строкой
    return matrix              # верните значение переменной matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)









