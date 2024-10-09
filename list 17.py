# Extract even numbers from a list.
n = int(input("Enter your N th number : "))
list = []
for i in range(n):
    a = int(input("Enter your list elements of list :"))
    list.append(a)

even = []
for i in list:
    if i % 2 == 0:
        even.append(i)

print("Even number list :")
print(even)

