"""
Topic: Dictonary In Python
"""

# thisDict = {"brand":"Ford", "model":"Mustang", "year":2004, "colors": ["red","yellow","black"]}
# print(thisDict)
# Type of Dict with the help of type() function
# print(type(thisDict))
# Length with len() function
# print(len(thisDict))

# Features of Dictonary in Python
# 1. Unchangeable
# 2. Duplicates Not Allowed

# Accessing Dictonary with the help of key
# {key: values}
# x = thisDict["model"]
# print(x)

# get() function
# y = thisDict.get("model")
# print(y)

# key() function
# ky = thisDict.keys()
# print(ky)

# values() function
# val = thisDict.values()
# print(val)

# items() function
# itm = thisDict.items()
# print(itm)

# Check If key exists
# if "model" in thisDict:
#     print("Yes")
# else:
#     print("No")


# Change Dictonary Items
# thisDict["year"] = 2018
# print(thisDict)

# thisDict.update({"year":"2022"})
# print(thisDict)

# Add Dictonary Items
# thisDict.update({"version":"GT"})
# print(thisDict)

# Remove Items 
# thisDict.pop("model")
# print(thisDict)

# thisDict.popitem()
# print(thisDict)

# del thisDict["year"]
# print(thisDict)

# thisDict.clear()
# print(thisDict)

# Loop Dictonaries
# thisDict = {"brand":"Ford", "model":"Mustang", "year":2004, "colors": ["red","yellow","black"]}
# for i in thisDict:
    # print(i) #keys
    # print(thisDict[i]) #values
    
# for i in thisDict.keys():
#     print(i)

# for i in thisDict.values():
#     print(i)

# for i,j in thisDict.items():
#     print(i, j)