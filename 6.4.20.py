#task1
#create a empty dictionary
#add below elements
#"hello": 5 (len of key)
#python:6
#val:3
#print all keys
#print all values
'''
#create a empty dictionary

dict1 = {}
print(type(dict1))


#add below elements

dict1 = {"hello": len("hello"),"python": len("python"),"val":len("val")}

print(dict1)

#print all keys

print(dict1.keys())


#print all values

print(dict1.values())

# Python Variables

'''

#Create a variable

a = "mahi"

b = 5

# output text and a variable

print(a)
print(b)

# Add a variable to another varible
c = b

print(c)

#Python Numbers

#verify the type of an object

print(type(c))
print(type(a))
print(type(b))

#create integers

d = 5
e = 1.5
f = 1e5
g = 5j

print(type(d))
print(type(e))
print(type(f))
print(type(g))

#python casting

#casting - intergers

print(type(int(d)))
print(type(float(e)))
print(type(str(f)))

#Python Strings

#get the character at position 1 of a string

string1 = "python"

print(string1[1])

#get characters from postion 2 to 5

print(string1[2:-1])

#remove white space from begining and end of string

string2 = " Python "

string3 = string2.strip()

print(string3)

#return length of string

print(len(string2))

#convert a string to lower case

string4 = string2.lower()

print(string4)

#convert a string to Upper case

string4 = string2.upper()

print(string4)

#replace string with another string

print(string2.replace("Python", "Mahi"))

#spit string into sub string

string5 = "Hello,Team"

print(string5.split(","))


#Python Operators

#Addition operator

a = 5
b = 10

c = (a+b)


print(c)

#Subtraction operator

d = (a-b)
print(d)

#multiplication operator

e = (a*b)
print(e)

#division

f = (a/b)

print("division:",f)

#modulus

print("modulus :", a%b)

#assignment operator

g = 25

print("assignment operator",g)

#python list

#create list

list1 = [1,2,3,4,5]

print("access list item :", list1[2])

#chnage the value of list item

list1.insert(3,10)
print(list1)

#loop through list

for list2 in list1:
    print(list2)

#check if list item exists

if 10 in list1:

 print("yes, 10 in this list1")

 print("get the length of list :", len(list1))

 list1.append("mahi")

 print("add item to end of list :" ,list1 )


 list1.insert(1,"hello")

 print("add item to specified index :", list1)

 list1.remove("mahi")
 print("remove an item ", list1)


 list1.pop()

 print("Remove last item :",list1)

 del list1[1]

 print("Remove specific Item from the index :",list1)


list1.clear()
print("empty list :", list1)

list5 = list(list1)
print("using list constructor to make list :",list5)

#Python Tuples

tuple1 = (1,2,3,4,5)

print("create tuple :",tuple1)

print("Access tuple items :",tuple1[1])

#change the tuple value

#tuple1[1] = "mahi"

print("changing the tuple1 value is not allowed in tuple1")

#loop through tuple

for x in tuple1:
    print(x)


#check if a tuple item exists

if 2 in tuple1:
    print("yes 2 is in tuple1")


print("get the length of tuple ", len(tuple1))

#delete tuple

del tuple1

#using tuple constructor to create tuple

tuple2 = tuple(("mh",1,2,3,4))

print("using tuple constructor to create tuple :",tuple2)

#Python Sets

#create a set

set1 = {1,2,3,4,5,9,"mahi"}

#loop through a set

for x in set1:
    print("loop through set:",x)

#check if an item exist or not

if "mahi" in set1:
    print("yes mahi is available")

#Add item to a set

set1.add("rockers")

print("Add item to set:",set1)


set1.update("m","a","h","i")

print("Add multiple items to the set :",set1)

print("get length of set :",len(set1))

set1.remove("rockers")

print("remove item from the set :",set1)

set1.discard("mahi")

print("remove item from set using discard method :",set1)

set1.pop()

print("remove last item from the set using pop :",set1)

set1.clear()

print("empty set :",set1)

#del set1

print("delete set :",set1)

#Using set constructor to create set

set2 = set((1,2,3,4,5))

print("Using set constructer to create set :",set2)

#Python Dictionaries

#create dictionary

dict1 = {"mahi":"python","cricket":"sports","workout":"gym"}

print("create dictionary:",dict1)

print("access the items of dictionary :",dict1["cricket"])

dict1["mahi"] = "AWS"

print("Chnaging the value of dictionary :",dict1)

#print all keynames in dictionary one by one

for x in dict1:
    print("print all key name in dictionary one by one:",x)

#print all values in dictionary one by one

for x in dict1:

    print("print all values in dictionary one by one :",dict1[x])

print("using value function to return the values of dictionary :",dict1.values())

for x,y in dict1.items():
    print("looping through both key and values using item function :",x,y)

#check if the key exists or not

if "mahi" in dict1:
    print("yes mahi exists ")


print("get length of dictionary :",len(dict1))


#add item to dictionary

dict1.update({"CCNA":"Security"})

print("Add item to the security :",dict1)

#remove item from dictionary

dict1.pop("mahi")

print("remove item from the dictionary :",dict1)

#empty dictionary

dict1.clear()
print("empty dictionary ")

#create dict using constructur

dict2 = dict(mahi = "python",AWS = "cloud")

print("create dict using constructor:",dict2)





























