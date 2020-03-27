'''
#capitalize()	Converts the first character to upper case

Name = "mahi"

a = Name.capitalize()
print(a)

#casefold()	Converts string into lower case

a = "MAHi"
b = a.casefold()
print(b)

#center()	Returns a centered string

a = "Mahi"

b = a.center(70)

print(b)

#count()	Returns the number of times a specified value occurs in a string

a = "i am mahi"
b = a.count("a")
print(b)

#encode()	Returns an encoded version of the string

i = "mahendra"

x = i.encode()

print(x)


#endswith()	Returns true if the string ends with the specified value

string = "Hello,"

x = string.endswith(".")

print(x)

#expandtabs()	Sets the tab size of the string

a = "M\ta\th\ti\ti"

x =  a.expandtabs(10)

print(x)


#find()	Searches the string for a specified value and returns the position of where it was found

a = "Hello, welcome to my world."

x = a.find("welcome")

print(x)


#format()	Formats specified values in a string



a = "My name is {}, I'am {}".format("mahi",26)

print(a)


#index()	Searches the string for a specified value and returns the position of where it was found

a = "Hello"

x = a.index("e")

print(x)


#isalnum()	Returns True if all characters in the string are alphanumeric

a = "Hello"

x = a.isalnum()

print(x)


#isalpha()	Returns True if all characters in the string are in the alphabet


a = "Hello"

x = a.isalpha()

print(x)

#isdecimal()	Returns True if all characters in the string are decimals

a = "12345"

x = a.isdecimal()

print(x)


#isdigit()	Returns True if all characters in the string are digits

a = "1235"

print(a.isdigit())


#isidentifier()	Returns True if the string is an identifier (A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.)

a = "_My"

print(a.isidentifier())


#islower()	Returns True if all characters in the string are lower case (Numbers, symbols and spaces are not checked, only alphabet characters.)

a = "_my 10 mm"

print(a.islower())


#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.Exponents, like ² and ¾ are also considered to be numeric values.

a = "23482353"

print(a.isnumeric())

#isprintable()	Returns True if all characters in the string are printable(Example of none printable character can be carriage return and line feed.)

a = "23482353"

print(a.isprintable())

#The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.

a = " "

print(a.isspace())


#The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.Symbols and numbers are ignored

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

#The isupper() method returns True if all the characters are in upper case, otherwise False.Numbers, symbols and spaces are not checked, only alphabet characters.
a = "HELLO, AND WELCOME TO MY WORLD"
print(a.isupper())


#The join() method takes all items in an iterable and joins them into one string.A string must be specified as the separator.
a= ("mahi","Mahii")

x = "#".join(a)

print(x)

#ljust()	Returns a left justified version of the string

a = "Apple"

print(a.ljust(20), "is my favorite fruit.")

#lower()	Converts a string into lower case
a = "Apple"

print(a.lower())

#The lstrip() method removes any leading characters (space is the default leading character to remove)

a = "   Apple"

print(a.lstrip())

#partition() (Returns a tuple where the string is parted into three parts)

a = "I am Mahi"

print(a.partition('Mahi'))

# The replace() method replaces a specified phrase with another specified phrase.

a = "Mahi"
print(a.replace("i","e"))

#The rfind() method finds the last occurrence of the specified value.

#The rfind() method returns -1 if the value is not found.

#The rfind() method is almost the same as the rindex() method. See example below.

a = "mahendran"
print(a.rfind("n"))

#rindex()	Searches the string for a specified value and returns the last position of where it was found

a = "mahendran"
print(a.rindex("a"))


#The rjust() method will right align the string, using a specified character (space is default) as the fill character.

a = "mahendran"

print(a.rjust(20))


#The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.

#The first element contains the part before the specified string.

#The second element contains the specified string.

#The third element contains the part after the string.


a = "lets play cricket"
print(a.rpartition("play"))



#The rsplit() method splits a string into a list, starting from the right.If no "max" is specified, this method will return the same as the split() method.


a = "lets play cricket"
print(a.rsplit(", "))

#The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

a = "cricket_"
print(a.rstrip("_"))

#The split() method splits a string into a list.You can specify the separator, default separator is any whitespace.
a = "My favorite sport is cricket"

print(a.split(" "))


#The splitlines() method splits a string into a list. The splitting is done at line breaks.

a  = "Hello\n Mr.mahendran"

print(a.splitlines())


#The startswith() method returns True if the string starts with the specified value, otherwise False.

a = "lets play cricket"
print(a.startswith("lets"))


#Remove spaces at the beginning and at the end of the string:
a = "_mahi_"
print(a.split("_"))


#The swapcase() method returns a string where all the upper case letters are lower case and vice versa.

a ="MaHiI"

print(a.swapcase())


#The title() method returns a string where the first character in every word is upper case. Like a header, or a title.If the word contains a number or a symbol, the first letter after that will be converted to upper case.
a = "mahendhiran kanagaraj"
print(a.title())

#upper()	Converts a string into upper case

a = "small letters"
print(a.upper())

#The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

#If the value of the len parameter is less than the length of the string, no filling is done.

a = "Mahi"

print(a.zfill(15))

'''




















