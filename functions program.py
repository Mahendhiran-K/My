# write a function to check wheather a string is palindrome or not
'''
def function(x):
    i = x[::-1]
    if x == i:
        print("palindrome")
    else:
        print("not Palindrome")

function(input("Enter the string to check :"))
'''
'''
#*************************************************************************#

#write a function to check wheather a number is odd or even

def number(x):
    if x % 2 == 0:
        print("The Number is even")
    else:
            print("The Number is ODD")

number(int(input("enter the value:")))

#*************************************************************************#
'''
'''
#write a function to check wheather a number is positive or negative

def number(x):
    if x > 0:
        print("The Number is positive")
    else:
            print("The Number is Negative")

number(int(input("Enter the Value :")))
'''
#************************************************************************#
'''
#get two numbers from user and do below process
#(a+b)(a-b)

def number(x,y):
    c = (x + y) * (x - y)
    return (c)

a = int(input("enter the value:"))

b = int(input("enter the value:"))

print(number(a,b))
'''
#**************************************************************************#

#get three numbers from user and do the below process
#(a+b)(a-b)(a-c)

def number (x,y,z):
    d = (x + b) * (x - b) * (x - c)
    return (d)
a = int(input("enter the value:"))

b = int(input("enter the value:"))

c = int(input("enter the value:"))

print(number(a,b,c))


