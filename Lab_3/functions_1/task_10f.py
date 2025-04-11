def unique_elements(lst):
    unique_lst = []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst
numbers = list(map(int, input("список чисел: ").split()))
print("уникальныe элементы:", unique_elements(numbers))