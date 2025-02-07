mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)

thislist.append("orange")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist.remove("banana")
print(thislist)

thislist.clear()
print(thislist)

thislist1 = ["apple", "banana", "cherry"]
for x in thislist1:
  print(x)



list1 = ["abc", 34, True, 40, "male"]
