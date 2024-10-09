# print positive and negative element of the list
n = int(input("Give your  :"))
list = []
for i in range(n):
    a= int(input("Enter your elements of string :"))
    list.append(a)

positive =[]
negative =[]
for i in list:
    if i < 0 :
        negative.append(i)
    else:
        positive.append(i)

print(f"positive : \n{positive} \nNegative : \n{negative}")