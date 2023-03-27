# thisTup = (1,2,3,4,5,6,7,8,9,0)
# print(thisTup)
# print(type(thisTup))

# Features of Tuple
# 1. Tuples are immutable (whereas lists are mutable) $Difference
# 2. Ordered 
# 3. Tuples allows us to store duplicates

# tup = (1,2,3,4,5,1,1,2)
# print(tup)

# Tuple length
# print(len(tup))

"""Access Tuples"""

tupl = ("apple","banana","cherry","DragonFruit","Guava")
# tuple[index] or list[index]
print(tupl[1])
print(tupl[-1])
# range - (start, end-1)
# tupl[start, end] -> start to end-1
print(tupl[1:4])

# If we don't give start index then what will happen
# Start from 0th index
print(tupl[:4])

# If we don't give end index then what will happen
# run til end index
print(tupl[2:])

# Check if item exists
if("apple" in tupl):
    print("Found")
else:
    print("Not Found")

"""Update Tuples"""
x = ("guava","grapes","apple","cherry")
y = list(x)
y[2] = "kiwi"
x = tuple(y)
print(x)

# append()
tp = ("apple","banana","guava")
y = list(tp)
y.append("orange")
tp = tuple(y)
print(tp)
# ('apple', 'banana', 'guava', 'orange') -> updated tuple

# remove()
y = list(tp)
y.remove("banana")
tp = tuple(y)
print(tp)

# del keyword
tp = ("apple","banana","guava")
del tp
# print(tp) # It will always give us an error bcoz tuple no longer exists in memory

"""Unpack Tuples"""
fruits = ("apple","banana","cherry", "dragonfruit", "rasberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)