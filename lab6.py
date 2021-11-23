#Program : String is palindrome or not..

string = input ("Please enter a string:")
text = ''

for i in string:
    text = i + text

if(text == string):
    print("This is a palindrome")  
else:
    print("This is not a palindrome")      