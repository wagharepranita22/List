# Find common elements between two lists.
n = int(input("Enter your N th number : "))
list1 = []
for i in range(n):
    a = int(input("Enter your list elements of list :"))
    list1.append(a)

n1 = int(input("Enter your N th number : "))
list2 = []
for i in range(n1):
    a = int(input("Enter your list elements of list :"))
    list2.append(a)


intersect = list(set(list2) & set(list1))
print("Intersection : ",intersect)
