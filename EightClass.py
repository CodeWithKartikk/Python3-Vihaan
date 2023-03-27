"""
Author: Kartik Kathuria
Topic: Python Lists
Date & Time: 12-02-23 & 3:34 P.M.
""" 

# Lists are used to store multiple items(collections of data) in a single variable
# listVar = [1,2,3,4,5,6,7,8] # List of Integers
# print(listVar)
# print(type(listVar)) # Type Function

# Characterstics of Lists in Pyhton
# 1. List Items
# 2. List is Ordered
# 3. Changeable (Mutable)
# 4. Allow Duplicates

# thisList = ["apple","cherry","banana","pineapple"] # List of Strings
# print(thisList)

# Length of the list - len()
# print(len(thisList)) # 4

# boolList = [True, False, True, True]

""" Acccess List Items"""
# Positive Indexing - (Left to right)
# Negative Indexing - (Right to left)
# Printinh Always Left to right
# thisList = ["apple","cherry","banana","pineapple"] # List of String
# print(thisList[1])
# print(thisList[-1])
# print(thisList[1:3]) # from start to end-1
# print(thisList[-4:-2])

"""Check If List Item exists or not"""
# print("Apple" in thisList)

"""Change Item Value"""
ls = ["apple","banana","cherry"]
print(ls)
ls[1] = "blackberry"
print(ls)

"""Insert Items"""
# listName.insert(index values. item value)
ls.insert(2, "watermelon")
print(ls)