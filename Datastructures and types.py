
# Data structures -

'''A data structure is used to store a data in organized way.
There are 4 types in data structures.
1. List
2.Tuple
3.Set
4.Dictionaries'''

#-----------------------------------------------------------------------------------------------------------#

#List : -

'''Key point of list:
==> It is enclosed in square brackets[]
==> Ordering and indexing is possible
==> Its mutable, we can modify the data in the list
==> Duplicates are possible in list
EX:
list1 = [1,2,3,"mahi","mahi2",4,5,6]'''


# Methods in List--

#append() -
'''  Adds an element at the end of the list
list1 = [1,2,3,4,5]
list1.append("Mahi")
print(list1)

==> Output - [1,2,3,4,5,"Mahi"]'''

#clear()-
'''- Removes all the elements from the list and it will keep empty bracket
list1 =  [1,2,3,4,5]
list1.clear()
print(list1)

==> output = []'''


#copy() -
'''returns a copy of the particular list.

list1 = [1,2,3,4,5]
list2 = list1.copy()
print(list2)

==> Output = [1,2,3,4,5]'''

 
#count() -
'''Returns the number of  duplicate elements with in the specified list
list1 = [1,2,3,4,5,5,5]
list2 = list1.count(5)
print(list2)

==> output = 3'''

#extend() -
'''adds the specified list elements (or any iterable) to the end of the current list.
list1 = [1,2,3,4,5]
list2 = [7,8,9]
list1.extend(list2)
print(list1)

==> Output = [1,2,3,4,5,7,8,9]'''

#index() -
'''returns the position at the first occurrence of the specified value.
list1 = [1,2,3,4,5,6]
x = list1.index(3)
print(x)

==> output = 2'''

#insert() -
'''Adds an element at the specified position
list1 = [1,2,3,4,5]
list1.insert(3,45)
print(list1)

==> output = [1, 2, 3, 45, 4, 5]'''

#pop()-
'''Removes the element at the specified position
list1 = [1,2,3,4,5]
list1.pop(2)
print(list1)

==> output = [1,2,4,5]'''

#Remove()-

'''Removes the item with the specified value
list1 = [1,2,3,4,5]
list1.remove(3)
print(list1)

==> output = [1,2,4,5]'''

#reverse() -

'''Reverses the order of the list
list1 = [1,2,3,4,5]
list1.reverse()
print(list1)
==> output = [5,4,3,2,1]'''

#Sort() -

''' Sorts the list from smallest to largest
list1 = [5,3,4,1,2]
list1.sort()
print(list1)
output = [1,2,3,4,5]'''

#------------------------------------------------------------------------------------------------------------#

#Tuple : -

'''Key points to remember of tuple:
* It is enclosed in round brackets()
* Ordering and indexing is possible
* Its immutable, we cannot change/update the tuple
* Duplicates are possible in tuple
EX:

tuple1 = (1,2,3,"Mahi","sports",4.5)'''


#Methods in tuple--

#count() -
'''Returns the number of times a specified value occurs in a tuple
tuple1 = (1,2,3,4,4,5,6,8)
tuple1.count(4)
print(tuple1)

==> output = 2'''

#index() -
'''Searches the tuple for a specified value and returns the position of where it was found
tuple1 = (1,2,3,4,5)
x = tuple1.index(3)
print(x)

==> output = 2'''


#-------------------------------------------------------------------------------------------------------#


#Set : -

'''key points of set:
* It is enclosed in curly brackets{}
* Ordering and indexing is not possible
* Its mutable, we can change/update the set
* Duplicates are not possible in set
E.g., set1 = {1,2,3,"Nandan",True,4.5}'''



#Methods in set -

#add() -
'''Adds an element to the set
set1 = {1,2,3,4,5}
set1.add(6)
print(set1)

==> output = {1,2,3,4,5,6}'''

#clear() -
'''Removes all the elements from the set
set1 = {1,2,3,4,5,6}
set1.clear()
print(set1)

==> output = {}'''

#copy() -
'''Returns a copy of the set
set1 = {1,2,3,4,5,7}
seb2 = set1.copy()
print(set2)

==> output = {1,2,3,4,5,7}'''

#differnce() -
'''Returns a set containing the difference between two or more sets
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set3 = set1.difference(set2)
print(set3)

==> output = {1,2,3}'''

#difference_update() -
'''Removes the items in this set that are also included in another, specified set
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set1.difference_update(set2)
print(set1)

==> output = {1,2,3}'''

#discard() -
''' Remove the specified item
set1 = {1,2,3,4,5,6}
set1.remove(4)
print(set1)

==> output = {1, 2, 3, 5, 6}'''

#intersection() -
'''Returns a set, that is the intersection of two other sets
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set3 = set1.intersection(set2)
print(set3)

==> output = {4,5,6}'''

#intersection_update() -

'''Removes the items in this set that are not present in other, specified set(s)
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set1.intersection_update(set2)
print(set1)

==> output = {4,5,6}'''

#isdisjoint() -
'''Returns whether two sets have a intersection or not
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
x = set1.isdisjoint(set2)
print(x)

==> Output = True

set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
x = set1.isdisjoint(set2)

print(x)

==> output = False'''

#issubset()-

'''Returns whether another set contains this set or not

set1 = {1,2,3,4,5,6,7,8,9,10}

set2 = {2,5,4,8,10}
x = set2.issubset(set1)
print(x)

==> output = True'''

#issuperset() -

'''Returns whether this set contains another set or not
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {2,5,4,8,10}
x = set1.issuperset(set2)
print(x)

==> output = True'''

#pop() -

'''Removes an element from the set
set1 = {1,2,3,4,5,6,7,8,9,10}
set1.pop()
print(set1)

==> output = {2,3,4,5,6,7,8,9,10}'''

#remove() -
'''Removes the specified element
set1 - {1,2,3,4,5,6}
set1.remove(3)
print(set1)

==> output = {1,2,4,5,6}'''

#symmetric_difference() -

'''Returns a set with the symmetric differences of two sets

set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
set3 = set1.symmetric_difference(set2)
print(set3)

==> output = {1,2,3,4,5,7,8,9,10}'''

#symmetric_difference_update() -

'''inserts the symmetric differences from this set and another
set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
set1.symmetric_difference_update(set2)
print(set1)

==> output = {1,2,3,4,5,7,8,9,10}'''

#union() -
'''Return a set containing the union of sets

set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
set3 = set1.union(set2)
print(set3)

==> output = {1,2,3,4,5,6,7,8,9,10}'''

#update()-

'''Update the set with the union of this set and others
set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
set1.update(set2)
print(set1)


==> output = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}'''


#------------------------------------------------------------------------------------------------------------#

#Dictionaries:

'''Key Points of dictioanies:

* It is a key value pair enclosed in curly brackets{:}
* Ordering and indexing is not possible
* Its mutable, we can change/update the dictionaries
* Duplicate keys are not possible but duplicate values are possible
EX:

dic1 = {"Mahi":"Python","Mahii":"Value","key":"value 2"}'''


#Methods in Dictionaries --

#clear() -
'''Removes all the elements from the dictionary

dic1 = {1:"Python",2:"Aws",3:"mcsa"}

dic1.clear()
print(dic1)

output = {}'''

#copy()-
'''Returns a copy of the dictionary
dic1 = {1:"Python",2:"Aws",3:"mcsa"}
dic2 = dic1.copy()
print(dic2)

==> output = {1:"Python",2:"Aws",3:"mcsa"}'''

#fromkeys() -
'''Returns a dictionary with the specified keys and value

key = {'AWS','Azure','python'}
value = 'devops'
dic1 = dict.fromkeys(key,value)
print(dic1)

==>  output =  {'Azure': 'devops', 'AWS': 'devops', 'python': 'devops'} '''

# get() -
'''Returns the value of the specified key
dic1 = {"Mahi":"Python","AWS":"Sysops","CCNA":"Networking"}
dic2 = dic1.get("Mahi")
print(dic2)

==> output= Python'''

#items() -

'''Returns a list containing a tuple for each key value pair
dic1 = {"Mahi":"Python","AWS":"Sysops","CCNA":"Networking"}
dic2 = dic1.items()
print(dic2)

==> output = dict_items([('Mahi', 'Python'), ('AWS', 'Sysops'), ('CCNA', 'Networking')])'''

#keys() -

'''Returns a list containing the dictionary's keys
dic1 = {"Mahi":"Python","AWS":"Sysops","CCNA":"Networking"}
dic2 = dic1.keys()
print(dic2)
output = dict_keys(['Mahi', 'AWS', 'CCNA'])'''

#values() -
'''Returns a list of all the values in the dictionary
dic1 = {"Mahi":"Python","AWS":"Sysops","CCNA":"Networking"}
dic2 = dic1.values()
print(dic2)

==> output = dict_values(['Python', 'Sysops', 'Networking'])'''

#pop() -

'''Removes the element with the specified key
dic1 = {"Mahi":"Python","AWS":"Sysops","CCNA":"Networking"}
dic1.pop("AWS")
print(dic1)

==> output = {'Mahi': 'Python', 'CCNA': 'Networking'}'''

#popitem() -
'''Removes the last inserted key-value pair
dic1 = {"Mahi":"Python","AWS":"Sysops","CCNA":"Networking"}
dic1.popitem()
print(dic1)

==> output = {'Mahi': 'Python', 'AWS': 'Sysops'}'''

#setdefault() -
'''Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
dic1 = {"Mahi":"Python","AWS":"Sysops","CCNA":"Networking"}
dic2 = dic1.setdefault("Abdul","kalam")
print(dic2)

==> output = kalam'''

#update() -
'''Updates the dictionary with the specified key-value pairs
dic1 = {"Mahi":"Python","AWS":"Sysops","CCNA":"Networking"}
dic1.update({"Abdul":"kalam"})
print(dic1)
output = {'Mahi': 'Python', 'AWS': 'Sysops', 'CCNA': 'Networking', 'Abdul': 'kalam'}'''



