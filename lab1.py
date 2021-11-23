# Program : Greeting..

name = input("Enter your name:")
age = input("Enter your age:")

#current year :2021
hundred_year = 2021 + (100 - int(age))
output = "Hello {} , You will become 100 years old in the year {}!"
print(output.format(name,hundred_year))