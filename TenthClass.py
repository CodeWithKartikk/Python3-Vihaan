"""
Author: Kartik Kathuria
Topic:  Loop Through Lists
Time & Date: 2:23 & 03/04/23
"""
# First Way

# For loop traversing in lists
ls = [1,2,3,4,5,6,7,8,9,10] # For loop says we have declaration, initialisation and increment/decrement. 
print(len(ls))
# for i in ls:
#     print(i)

# for i in range(len(ls)):
#     print(ls[i])

# Second Way

# while loop traversing in lists (initialisation -> While(condition) -> Statements under loop) -> increment or decrement
# i = 0 # initialisation
# while i<len(ls): #while(condition)
#     print(ls[i]) #print
#     i = i+1 #increment

# Third Way (Direct or Expanded Method through for)
# [print(var name) for varName in listName]
[print(x) for x in ls]    

# Sort the lists
# Sort in Ascending order
# ls = [1,9,2,8,3,7,4,6,5]
# ls.sort() #Ascending
# ls.reverse()
# print(ls)
# ls.sort(reverse = True) #Descending
# print(ls)

# Sort in strings (Case Insensitive sort)
# myList = ["banana", "orange", "Kiwi", "cherry"]
# myList.sort()
# print(myList)