"""
Author: Kartik Kathuria
Topic: String Builtin methods
Date and Time: 28-01-23 & 12:47
"""

# --------> 1. capitalize() --> It converts the first character to uppercase
# str = "vihaan"
# cap = str.capitalize()
# print(cap)

# --------> 2. casefold() and lower() --> It converts sring into lowercase
# str1 = "VaIbHaV"
# caf = str1.casefold()
# lower = str1.lower()
# print(caf)
# print(lower)

# --------> 3. center() --> Returns a centered string 
# st = "banana"
# a = st.center(40)
# print(a)

# --------> 4. count() --> Returns the no. of times a "specified" value occurs in a string.
# str2 = "I love apples, apples are red and apples are my favourite fruit"
# cnt = str2.count("apples")
# cnt1 = str2.count("are")
# print(cnt)
# print(cnt1)

# --------> 5. encode() --> Returns an encoded version of the string.
# str3 = "My name is Vihaan"
# enc = str3.encode()
# print(enc)

# --------> 6. endswith() --> Returns True if the string ends with the specified value (boolean function)
# str4 = "He is playing Football"
# end = str4.endswith("Cricket")
# print(end)

# --------> 7. expandtabs() --> sets the tab size of the string
# ext = "H\te\tl\tl\to\t"
# tabs = ext.expandtabs(3)
# print(ext)
# print(tabs)

# --------> 8. find() --> searches the string for a specufued value and returns the position of where it was found.
# ftext = "Hello, welcome to the coding world"
# fin = ftext.find("welcome")
# print(fin)

# --------> 9. format() --> formats specified values in a string
# formatTxt = "My macbook price is {} rupees"
# print(formatTxt.format("85000"))

# --------> 10. index() --> searches the string for a specufued value and returns the position of where it was found.
# itext="Hello, welcome to the coding world."
# print(itext.index("Hello"))

# --------> 11. isalnum() --> Returns true when all characters in the string is alphanumeric.
# cr = "cristiano7"
# print(cr.isalnum())

# --------> 12. isalpha() --> Returns true when all characters in the string are alphabets.
# vi = "virat"
# print(vi.isalpha())

# --------> 13. isdecimal() --> Returns true when all characters in the string are decimals.
# num = "555"
# print(num.isdecimal())

# --------> 14. isdigit() --> Returns true when all characters in the string are digits.
# cr = "cristiano7"
# print(cr.isdigit())

# --------> 15. isnumeric() --> Returns true when all characters in the string are numeric.
# num = "555"
# print(num.isnumeric())

# --------> 16. islower() --> Returns true when all characters in the string are in lowercase.
# lwr = "kartik"
# print(lwr.islower())

# --------> 17. isupper() --> Returns true when all characters in the string are in uppercase.
# upr = "VIHAAN"
# print(upr.isupper())

# --------> 18. isprintable() --> Returns true when all characters in the string are prinable.
# ipa = "Hello! Are You #1?"
# print(ipa.isprintable())

# --------> 19 isspace() --> Returns true when all characters in the string are whitespaces.
# isp = "     "
# print(isp.isspace())

# ---------> 20. title() --> Converts the first character of each word to upper case. 
# txt = "Welcome to my arena warehouse"
# x = txt.title()
# print(x)
# Welcome To My Arena Warehouse

# --------> 21. istitle() --> Returns true if the string follows the rule of title.
# ist = "Hello, And Welcome To My World!"
# print(ist.istitle())

''' 22. ljust() -> It returns the left justified version of the strings '''

# txt = "banana"
# ljustVar = txt.ljust(20)
# print(ljustVar, "is my favorite fruit")

''' 23. rjust() -> It returns the right justified version of the strings '''

# txt = "banana"
# rjustVar = txt.rjust(20)
# print(rjustVar, "is my favorite fruit")

''' lstrip() -> Returns a left trim version of the string'''
''' rstrip() -> Returns the right trim version of the string'''

# text = "          banana          "
# x = text.lstrip()
# y = text.rstrip()
# z = text.strip()
# print(x)
# print(y)
# print(z)

''' maketrans() -> Returns a translation tableto be used in translation '''
# txt = "Hello, Gaurabh"
# mytable = txt.maketrans("G","S")
# print(txt.translate(mytable))

''' replace() -> returns a string where a specified value is with a specified value '''
# txt = "I love bananas"
# x = txt. replace("bananas", "Apples")
# print(x)

''' rfind() -> searches the string for a specified value and returns the last position of where it was found '''
# txt = "Mi casa, su casa."
# z = txt.rfind("casa")
# print(z)

''' rindex() -> searches the string  for a specified value and returns the last position of where it was found'''
# txt = "I am Kartik kathuria, Method was developed by kartik kathuria"
# rVar = txt.rindex("kathuria")
# print(rVar)

''' splitlines() -> splits the string at line breaks and returns a list'''
# txt = " Thank You for the music\nWelcome to My World"
# x = txt.splitlines()
# print(x)

''' split() -> Splits the string at the specified operaror, and returns a list'''
# txt = "Welcome to the jungle"
# x = txt.split()
# print(x)

''' startswith() - Returns True if the string starts with the specified value, otherwise False. '''
# txt = "Hello this is my arena"
# stVar = txt.startswith("Hello")
# print(stVar)

''' swapcase() - Swaps cases, lower case becomes upper case and vice versa. '''
# txt = "hELLO tHIS iS kARTIK"
# x = txt.swapcase()
# print(x)

''' zfill()      - Fills the string with a specified number of 0 values at the beginning. '''
# txt = "5154515"
# x = txt.zfill(10)
# print(x)

''' --------- THANK YOU! ----------- '''