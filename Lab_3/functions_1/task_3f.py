def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2  #кролик
    x = numheads - y  #курица
    
    return x, y
numheads = int(input("Введите количество голов: "))
numlegs = int(input("Введите количество ног: "))

chickens, rabbits = solve(numheads, numlegs)

print(f"курицы: {chickens}")
print(f"кролики: {rabbits}")