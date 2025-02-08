def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
numbers_input = input("Введите список чисел: ")
numbers = list(map(int, numbers_input.split()))

prime_numbers = filter_prime(numbers)

print("Простые чилса из списка:", prime_numbers)