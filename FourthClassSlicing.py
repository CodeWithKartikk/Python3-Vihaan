"""Slicing Strings"""
st = "Hello,_World!"
print(st[2:6]) # from 2 to (6-1)

# Slice from the start
print(st[:7])

# Slice to the end
print(st[3:])

# Negative Indexing
# H   e   l   l   o   ,   _   W   o   r   l   d
# 0   1   2   3   4   5   6   7   8   9  10  11
# -12 -11 -10 -9 -8  -7  -6  -5  -4  -3  -2  -1
print(st[-5:-2])

# Positve - (start to end-1)
# negative - (start+1 to end)

"""Modify Strings"""
st = "Hello, Morld!"
print(st.upper())
print(st.lower())
print(st.strip())
print(st.replace("M","W"))

"""String Concatenation"""
a = "Hello"
b = "Vihaan"
c = a + " " + b
print(c)