# Program :  List comprehension
# Write one line of Python that takes a list and makes a new list that has only ,
#  the even elements of the list in it.

a =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = [i for i in a if(i%2 == 0)]
print(new_list)