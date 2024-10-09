#  Count the occurrence of a specific element in a list.
n = int(input("N :"))
list = []
for i in range(n):
    a = int(input("Enter your list element : "))
    list.append(a)

find = int(input("give your element to find the occurrence of element :"))
count = list.count(find)
print(f"Occurrence of {find} : {count}")