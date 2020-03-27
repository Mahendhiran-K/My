'''
#Task 1: #Get Input from User and try to convert second last and second to capital letter (pYthOn)
a = input("Enter the Value:")
print(a[0]+a[1].upper()+a[2:-2]+a[-2].upper()+a[-1])


#Task 2: get one sring from usr ("python),get one number from user (7)) output string * length.

a = input("enter the string:")
b = int(input("enter the value :"))
c = str(b)
d = len(a)

print((b*a)+(d*c))


#Task 3: get one string from user(python),convert 1st middle,last letter i to caps

a = input("enter the string:")
b = len(a)//2

print(a[0].upper()+a[1:b]+a[b].upper()+a[b+1:-1]+a[-1].upper())


#task 4: get two strings from suer(python,java) convert first letter ans last letter in caps in both strings.

a = str(input("enter the string A:"))
b = str(input("enter the string b:"))

print(a[0].upper()+a[1:-1]+a[-1].upper()+b[0].upper()+b[1:-1]+b[-1].upper())


#task 5: get two numbers from user (3,5) o/p 55533333

a = int(input("enter the value:"))
b = int(input("enter the value:"))
c = str(a)
d = str(b)

print(d*a+c*b)
'''


