# find the second max element
n = int(input("give your length of list :"))
list = []
for i in range(n):
    a = int(input("Enter your Element of the string :"))
    list.append(a)

max = 0
s_max = 0
index =0
s_index =0
for i in range (len(list)):
    if max < list[i]:
        s_max = max
        max = list[i]
        s_index = index
        index = i
    elif s_max < list [i]:
        s_max = list[i]
        s_index =i
print("Second max =",s_max)
print("Second max index",s_index)
