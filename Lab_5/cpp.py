def down(n):
    for i in range(n,-1,-1):
        yield i
for nums in down(int(input())):
    print(nums)