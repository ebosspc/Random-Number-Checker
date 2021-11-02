import random
 
list = []
def print_list():
    print("This is the list:")
    print(*list, sep = ', ')
 
for i in range(100):
    rand_num = int(random.randint(1,500))
    list.append(rand_num)
 
list.sort()
list.reverse()
 
user_num = int(input("Please enter a number to check if it is in the array: "))
 
if user_num in list:
    print("That nuber is in the array!")
    print("This is how many times it appears in the array: ")
    print(list.count(user_num))
 
else:
    print("Sorry, that is not in the array.")
 
print("This is the largest number:", max(list))
print("This is the smallest number:", min(list))
 
print_list()
