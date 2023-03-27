# myset = {"apple","banana","cherry"}

# Characterestics of Set
# 1. Duplicates Not Allowed
# 2. Unordered
# 3. Unchangeable (immutable)

# mySet = {"Apple","Banana","Cherry","Banana"}
# print(mySet)

# Length of the set
# print(len(mySet))

# type 
# print(type(mySet))

# Accessing Loops
# for i in mySet:
#     print(i)

# print("Banana" in mySet)

# Add Set Items
# mySet.add("Orange")
# print(mySet)

# mySet1 = {"Apple","Banana","Cherry"}
# fruits = {"pineapple","mango","papaya"}

# mySet1.update(fruits)
# print(mySet1)

# Remove Set Items
# remove()
# mSet = {"Cherry","Papaya","Grapes"}
# mSet.remove("Grapes")
# print(mSet)

# discard()
# mset1 = {"Cherry","Papaya","Grapes"}
# mset1.discard("Papaya")
# print(mset1)

# pop()
mset2 = {1,2,3,4,5,6}
x = mset2.pop()
print(x)
print(mset2)

# clear()
mset2.clear()
print(mset2)

# del keyword
# st = {1,3,5,7,9}
# del st
# print(st)

"""Loops in Sets"""
newSet = {1,2,3,4,5,6,7,8,9}
for i in newSet:
    print(i)

"""Joins in Sets"""

# union()
s1 = {1,2,3}
s2 = {"a","b","c"}
s3 = s1.union(s2)
print(s3)

# update()
s1.update(s2)
print(s1)

# intersection
st1 = {1,2,3,4,5,2,3,5}
st2 = {1,2,3,5,7,9}
st3 = st1.intersection(st2)
print(st3)

# intersection_update()
st1.intersection_update(st2)
print(st1)

# symmetric_difference()
x = {"apple","banana","cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# symmetric_difference_update()
x.symmetric_difference_update(y)
print(x)