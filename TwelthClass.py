"""List Methods in Python"""

# 1. append() - adds an element at the end of the list
# fruits = ["Apple","Banana","Cherry"]
# listName.append(value)
# fruits.append("DragonFruit")
# print(fruits)

# 2. clear() - removes all the elements from the list
# cr = [1,2,3,4,5,6,7,8]
# listName.clear()
# cr.clear()
# print(cr)

# 3. copy() - returns a copy of the list
# org = [1,2,3,4,5]
# listName.copy()
# cpy = org.copy()
# print(cpy)

# 4. count() 
# cnt = [1,2,3,4,5,3,5,7,8,9,0,3]
# listName.count(value)
# x = cnt.count(3)
# print(x)

# 5. extend()
# fru = ['Apple', 'Banana', 'Cherry', 'DragonFruit']
# car = ["Volvo", "BMW", "Tata", "Mahindra"]
# fru.extend(car)
# print(fru)

# 6. index() - returns index of the that element with the specified value
# fruit = ['Apple', 'Banana', 'Cherry', 'DragonFruit']
# x = fruit.index("DragonFruit")
# print(x)

# 7. insert() - Adds an element at the specified position/index
# fruit = ['Apple', 'Banana', 'Cherry', 'DragonFruit']
# listName.insert(index, value)
# fruit.insert(3, "Grapes")
# ['Apple', 'Banana', 'Cherry', 'Grapes', 'DragonFruit'] -> Uptaded Fruit list
# print(fruit)

# 8. pop() - removes the element at the specified position (removes the emlement present at last)
# fruit.pop()
# print(fruit)

# 9. remove() - removes the element at the specified value
# fruit.remove("Apple")
# print(fruit)

# 10. reverse() - reverse the order of the list 
# revLs = [1,2,3,4,5,6,7,8]
# revLs.reverse()
# print(revLs)

# 11. sort()

# Sort in ascending order
sortList = [1,3,5,7,9,0,8,6,4,2]
sortList.sort()
print(sortList)

# sort in descending order
sortDesc = [2,4,6,8,0,1,3,5,7,9]
sortDesc.sort(reverse=True)
print(sortDesc)