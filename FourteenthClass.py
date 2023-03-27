"""Loops Tuples"""
tp =  ("apple","banana","cherry")

# using for loop
# declaration and initialisation / condition / increment or decrement
# for i in tp:
#     print(i)

# for i in range(len(tp)):
#     print(tp[i])

# use while loop
# declaration and initialisation
# while "condition"
#    statements
#    increment / decrement
i = 0 # declare and initialise
while i<len(tp):
    print(tp[i])
    i = i + 1

# Join Tuples
tup1 = ("A", "B", "C")
tup2 = ("a", "b", "c")
tup3 = tup1 + tup2
print(tup3)

mytp = tp*2
print(mytp)

# Methods of Tuple
# 1. count()
tp = (1,2,3,4,5,6,2,4,7,2,8,9,2)
x = tp.count(2)
print(x)

# 2. index()
tp1 = (1,3,5,7,9)
y = tp.index(7)
print(y)