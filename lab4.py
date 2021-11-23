# Program : input a number from user,print a list of all the divisor of that number..

number = int(input("Enter a number:"))
divisors_list = []
i = 1
while (i< number):
    if(number%i == 0):
        divisors_list.append(i)
    i = i+1
print(divisors_list)



