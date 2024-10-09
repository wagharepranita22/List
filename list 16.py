# Reverse the elements of a list.
n = int(input("N : "))
list =[]
for i in range(n):
    a = input("ENetr your elements of list :")
    list.append(a)

revers =[]
for i in range(len(list)-1,0,-1):
    revers.append(list[i])

print("Give your reversed list :")
print(revers)
