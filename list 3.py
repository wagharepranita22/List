# print list in reversed order
n= int(input("Enter your N th element :"))
list = []
for i in range(n):
    a=input("GIve your list element :")
    list.append(a)

reversed = []
for j in range(len(list), 0, -1):
    reversed.append(list[j-1])

print(reversed)