# Task 1.2.2
# 1.Write a Python program to multiply all the items in a list.
list = [1, 5, 6, 9, 9] #can contain also one string
prod = 1
for i in list:
    prod *= i
print(prod)

# 2.Write a Python program to get the largest number from a list.
# this was in 1.2.1. lets use loops this time
list = [45, 85, 0, -6, 89, 1]
maxValue =list[0];
for i in list:
   thisNum = i
   if thisNum > maxValue:
      maxValue = thisNum
print(maxValue)


# 3.Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)
i = 1
n = 5
list = []
while i <= 30:
    list.append(i**2)
    i = i + 1
print(list[n:])


# 4.Write a Python program to remove duplicates from a list
list = [1, 2, 1, 3, 5, 1, 5]
i = 0
while i < len(list):
    j = i + 1
    while j < len(list):
        if list[i] == list[j]:
           list.pop(j)
        else:
            j += 1
    i += 1
print(list)

#using built in function
mylist = [1, 5, 3, 6, 3, 5, 6, 1]
mylist = list(set(mylist))
print (str(mylist))




# 5.Write a Python program to find the most appeared element in a list.
list = [2,5,6,2,8,8,9,2]
counter = 0
mostFreqNum = list[0]

for i in list:
    current_frequency = list.count(i)
    if (current_frequency > counter):
        counter = current_frequency
        mostFreqNum = i
print(mostFreqNum)



