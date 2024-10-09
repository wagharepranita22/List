# Given a list of numbers, find the sum, average, maximum, and minimum values.
# Given a list of numbers
n = int(input("N : "))
list = []
for i in range(n):
    a = int(input("Enter your element of array :"))
    list.append(a)
print(list)

# find the sum
sum = 0
for i in list:
    sum += i

print("sum of array element : ", sum)


# average
average = sum//n
print("average : ", average)

# maximum
print(max(list))

# minimum values.
print(min(list))