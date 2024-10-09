import logging

list = [23, 45, 1, 2, 34, 5, 8, 1, 2, 1, 1]
# Append
# list.append(123)
# print(list)
# Sort
# list.sort()
# print(list)

# reverser sort
# list.sort(reverse=True)
# print(list)

# reverse
# list.reverse()
# print(list)

# index
# print(list.index(1))

# count
# print(list.count(1))

# copy
m = list.copy()
m[1] = 0
# print(m)
# print(list)

# insert
# list.insert(0,3)
# print(list)

# extend
list.extend(m[1:3])
print(list)

# conctination
k = m+list
print(k)