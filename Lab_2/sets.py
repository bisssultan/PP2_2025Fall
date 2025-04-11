thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset1 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset1)

for x in thisset:
  print(x)

thisset.add("orange")
print(thisset)
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset.remove("banana")
print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

