# check if list is sorted or not
n = int(input("Give your n length :"))
list = []
for i in range (n):
    a = int(input("Enter your element :"))
    list.append(a)

for i in range (len(list)-1):
    if list[i] < list[i+1]:
        continue
    else:
        print("list is not sorted")
        break
else:
    print("List is sorted ")