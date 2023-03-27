"""Copy Lists"""

# ls1 = [1,2,3,4,5,6,7,8]
# ls2 = ls1 # assigning
# print(ls2)

# You cannot copy a list by typing list2 = list1, list2 will only be a refernce to a list1, and changes made in list1 will automatically alsi be made in list2.

# copy()
# thisList = ["apple", "banana", "cherry", "pineapple"]
# myList = thisList.copy() # create copy and assign it to myList
# print(myList)

# list()
# myNewList = list(thisList)
# print(myNewList)

"""Join Two Lists"""
ls1 = ["a", "b", "c"]
ls2 = [1,2,3]
# ls3 = ls1 + ls2
# print(ls3)

# Joining using for loops
# for i in ls2:
#     ls1.append(i)

# print(ls1)

# extend() method
# ls1.extend(ls2)
# print(ls1)