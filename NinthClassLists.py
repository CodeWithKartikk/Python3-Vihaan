"""
Author: Kartik Kathuria
Topic: List Actions (Function)
Date & Time: 19-02-2023 & 12:16
"""

"Adding List Items"
# insert(), append() - For Adding
# append() - Add an item at the end of the list
# ls = [1,2,3,4,5,6,7,8]
# ls.append(10)
# print(ls)

# insert() - Add an item at particular index
# insert(index, value)
# ls.insert(4, 9)
# print(ls)

# extend list
# extend() - To append elements from another list to the current list
# ls1 = ["apple","banana","cherry"]
# ls2 = ["mango","pineapple","papaya"]
# print(ls1)
# print(ls2)
# ls1.extend(ls2)
# print(ls1)

# Add any iterable
# ls3 = ["Apple", "peach", "banana"]
# tup = ("kiwi","dragonfruit","orange")
# ls3.extend(tup)
# print(ls3)

"""Remove List Items"""
# remove(), pop(), del keyword, clear()
# ls4 = [1,2,3,4,5,6,7]
# syntax - listName.remove(value)

# remove(value) - removes the specified value
# ls4.remove(3)
# print(ls4)

# pop(index) - removes the specified index
# ls4.pop(5)
# print(ls4)

# del keyword - also removes the specified index
# del listnam(index)
# del ls4[0]
# print(ls4)

# del is also used to delete the list as well
# del ls4
# print(ls4)

# clear the list
# ls5 = [1,2,3,4,5,6,7,8,9,0]
# print(ls5)
# ls5.clear()
# print(ls5)