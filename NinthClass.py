"""
Author: Kartik 
Topic: Operators Remaining Portion
"""

"""Python Comparison Operators"""
# ==, !=, >, <, >=, <=

# 1. == -> It simply returns a boolean(true or false)
x = 7
y = 9
z = 10
# print(x == y) # False

# 2. != (Not Equal to)
# print(x!=y) // True

# 3. >, <, >=, <= 
# print(x>y) # false
# print(x<y) # true
# print(x>=y) 
# print(x<=y)

"""Python Logical Operators - and, or, not"""
# and - Returns True if both statements are true 
# or - Returns True if any one of the statements is True
# not - Returns the result true if it is false, False if it is True
# print(x<5 and x<10) # false
# print(x<5 or x<10) # true
# print(not(x<5 or x<10)) # false

"""Python Identity Operators"""
# is - Returns True if both variables are the same object
# is not - Returns True if both variables are not the same object
print(x is z)
print(x is not y)
print(y is not z)

"""Pyhton Membership Operators"""
# in - Returns True if a sequence with the specified value is present in the object
# not in - Returns True if a sequence with the specified value is not present in the object

p = [1,2,3,4,5,6]
print(4 in p) # True
print(9 not in p) # True