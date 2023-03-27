"""
Author: Kartik Kathuria
Topic: Strings
Date & time: 22/01/23 11:42
"""

print('hello')
print("hello")

# Assign string to a variable
name = "Vihaan"
print(name)

# Multi Line Strings
para = """Hi
My Name is
Kartik Kathuria, I am 
a cloud engineer
at Hanu 
Softwares"""
print(para)

# Strings are Arrays
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# H e l l o , _ P y t h o n !
st = "Hello, Python!"
print(st[4])
print(st[6])

# String Length
print(len(st))

# Check String (in operator)
txt = "Hi Vihaan, Welcome to the world of Python!"
print("to" in txt)
print("of" in txt)

# Check if Not (Not in)
print("Kartik" not in txt)
print("world" not in txt)