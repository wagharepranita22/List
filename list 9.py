# print elemnt at one only
n= int(input("Enter your N th element :"))
list = []
for i in range(n):
    a=int(input("GIve your list element :"))
    list.append(a)

list=set(list)
print(list)