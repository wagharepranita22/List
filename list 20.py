# Merge two lists into a list of tuples.
n = int(input("Enter your N th number : "))
list1 = []
for i in range(n):
    a = int(input("Enter your list elements of list :"))
    list1.append(a)

n = int(input("Enter your N th number : "))
list2 = []
for i in range(n):
    a = int(input("Enter your list elements of list :"))
    list2.append(a)

zip = list(zip(list1, list2))
print(zip)
