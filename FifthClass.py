"""
Author: Kartik Kathuria
Topic: Format Strings and Escape Characters
Date & Time: 28-01-23 & 12:05
"""

# String Format
age = 14
txt = "My name is Vihaan, and I am {} years old"
print(txt.format(age))

# Example 1 on String Format
qty = 3 #0
itemno = 567 #1
price = 5000 #2
myOrder = "I want {} pieces of item {} for {} rupees"
print(myOrder.format(qty, itemno, price))

# Example 2 on String Format
myOrder2 = "I want to pay {2} rupees for {0} pieces of item {1}"
print(myOrder2.format(qty, itemno, price))

# txt = I want to make "2" litres of banana shake for "50" grams of protein intake.

"""Escape Characters""" 
# \followed by one character that u want to insert

# 1. \' - (') Single quote insertion
s = 'It\'s alright'
print(s)

# 2. \\ - (\) Backslash insertion
st = "This will insert one backslash \\"
print(st)

# 3. \n - For New Line
txt = "Hello\nWorld!"
print(txt)

# 4. \r - Carriage return
txt1 = "Hello\rWorld!"
st1 = "Hello Vihaan\rKartik this side"
print(txt1)
print(st1)

# 5. \t - Insert Tab Spaces
tabStr = "Hello This will insert \t Tab Space" 
print(tabStr)

# 6. \b - backspace one character
bacStr = "Hello\bWorld!"
print(bacStr)