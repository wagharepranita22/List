# find the max element of string and its index
n = int(input("Enter your length of the string :"))
list= []
for i in range(n):
    a= int (input("Enter your elements of the string :"))
    list.append(a)

max=0
index=0
for i in range(len(list)):
    if max < list[i]:
        max = list[i]
        index = i

print(f"Max =  {max}")
print(f"Index = {index}")