# Sort a list of strings in alphabetical order.
n = int(input("N :"))
list = []
for i in range(n):
    a = input("Enter your list element : ")
    list.append(a)

sort = sorted(list)
print("Here is your sorted list :")
print(sort)