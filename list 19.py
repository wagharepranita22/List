# Find the second largest number in a list.
n = int(input("Enter your N th number : "))
list1 = []
for i in range(n):
    a = int(input("Enter your list elements of list :"))
    list1.append(a)


list1.remove(max(list1))
print(max(list1))
