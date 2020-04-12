#pgm1
#check whether a string is palindrome or no

'''
string1 = input("enter the string input:")


if string1 == string1[::-1]:
    print("palindrome")
else:
    print("no palindrome")
'''
'''
#get a mark from student ()
#0 - 100 ==> valid

#100 grade a

#90 to 99 grade b

#80 to 89 grade c

#70 to 79 grade d

#50 to 69 grade e

# 0 to 49 fail grade f


#otherwise ===> invalid



mark = int(input("enter the marks:"))


if mark <= 100:
    print("valid")

if mark == 100:
    print("grade A")
elif mark >89 and mark <= 99:
    print("grade b")
elif mark >79 and mark <= 89:
    print("grade c")
elif mark >69 and mark <= 79:
    print("grade d")
elif mark >49 and mark <= 69:
    print("grade e")
elif mark >0 and mark <= 49:
    print("grade f")
else:
    print("invalid mark")
'''
'''
#pgm3
#check whether first char, middle char, last char of a string is same or different


#avvacca ==> True

#hello ==> False




string1 = str(input("enter the string:"))

mid = len(string1)//2

if string1[0]== string1[mid] == string1[-1]:
    print("True")
else:
    print("False")

#pgm4
#get two numbers from user

# 27

# 9

# True if sum 0f first no equal to second no (2 + 7 = 9)
# otherwise False


a = int(input("enter the value"))

b = int(input("enter the value"))

val = int(str(a)[0])
val1 = int(str(a)[1])


if val+val1 == b:
    print("True")
else:
    print("False")
    




#pgm5

#check whether a vowel present in a string and print no of occurences
#python  ==> available 1
#fst ==> not available 0
#bengaluru ==> available 4
    

#print even numbers from user input between the range using while

a = int(input("enter the value:"))
b = int(input("enter the value:"))

while a < b :
    if a % 2 == 0:
        a = a + 2
        print (a)
    elif a % 2 != 0:
    
        a = a + 1
        print (a)


    
        
#multiplies of 5 between 100 to 200

a = int(input("enter the value:"))
b = int(input("enter the value:"))

while a < b:
    if a%5==0:
        a = a + 5
        print (a)


#multiplies of 8 between given input

a = int(input("enter the value:"))
b = int(input("enter the value:"))

while a < b:
    if a%8==0:
        a = a + 8
        print (a)
    elif a % 8 !=0:
        a = a + 7
        print(a)
'''


##with/without vowel check
'''["hello", "bcd", "gcd", "hhmmm", "python"]

with vowels ["hello","python"]
without vowels ["bcd", "gcd", "hhmmm"]'''
'''
#starts with, ends with 
["hello", "bcd", "gcd", "hhmmm", "python"]

starting with h ["hhmmm", "hello"]
others
'''
'''
a = ["hello", "bcd", "gcd", "hhmmm", "python"]

with_vowel = []

without_vowel = []

for i in a:
    if ("a" in i or "e" in i or "i" in i or "o" in i or "u" in i or "A" in i or "E" in i or "I" in i or "O" in i or "U" in i):
        with_vowel.append(i)
        
    else:
        without_vowel.append(i)
        

print("list with vowel:",with_vowel)
print("list without vowel :",without_vowel)
'''
'''
#starts with, ends with 

a = ["hello", "bcd", "gcd", "hhmmm", "python"]

strlist = []
endlist = []

for i in a:
    if "h" in i[0]:
        strlist.append(i)
    else:
        endlist.append(i)
print ("starting with :",strlist)
print("ending with :",endlist)
'''
    
    
#pgm5

#check whether a vowel present in a string and print no of occurences
#python  ==> available 1
#fst ==> not available 0
#bengaluru ==> available 4

i = input("enter the value:")
if (i = "a"  or i= "e" or i = "i"  or i="o" or i = "u"):
    print(i)
    
    
    
    




