# Check if a specific number is present in a list.
n = int(input("N :"))
list = []
for i in range(n):
    a = int(input("Enter your list element : "))
    list.append(a)

i = int(input("Enter your element to verify if is present in list or not : "))
if i in list:
    print("Yes ! element is present in list")
else:
    print("No ! is not present in list")