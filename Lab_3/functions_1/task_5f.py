import itertools

def print_permutations():
    user_input = input("строка: ")
    permutations = itertools.permutations(user_input)
    for perm in permutations:
        print(''.join(perm))

print_permutations() 