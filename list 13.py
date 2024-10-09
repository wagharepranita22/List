# Remove duplicates from a list and return a list with unique elements.
n = int(input("N :"))
list = []
for i in range(n):
    a = int(input("Enter your list element : "))
    list.append(a)

set = set(list)
print(set)