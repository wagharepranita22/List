# pallindrom
n= int(input("Enter your N th element :"))
list = []
for i in range(n):
    a=int(input("GIve your list element :"))
    list.append(a)
copy =list.copy()
reversed = []
for j in range(len(list), 0, -1):
    reversed.append(list[j-1])

print(reversed)
if reversed == copy:
    print("List is pallindrome ")
else:
    print("List is not pallindrome")