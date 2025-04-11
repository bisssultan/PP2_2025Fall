def histogram(numbers):
    for num in numbers:
        print('*' * int(num))  # Преобразуем строку в число вручную

numbers = input("числa: ").split()  # Получаем список строк
histogram(numbers)