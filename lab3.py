# Program : To print all the elements in the list less than 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("Original list : {}".format(a))

new_list = []
print("All the elements in the list that are less than 5 is: ")
for x in a:
    if(x<5):
        new_list.append(x)
print(new_list)