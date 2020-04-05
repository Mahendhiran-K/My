'''
#task 1

#create empty list
#concatenate it with [5,6,8,9]
#add 8,9,1,5,6,7,8
#find no of occurence of 8
#find average of the list
#find sum of list + min ele + max ele of list
#find mean median of list
#remove duplicates from concatenated list and give output in tuple format

#create empty list
list1 = []
print("emtpty list : ",list1)
print(type(list1)

#concatenate it with [5,6,8,9]
list2 = [5,6,8,9]
con = list1+list2
print("concatenate output :",con)

#add 8,9,1,5,6,7,8

con.append(8)
con.append(9)
con.append(1)
con.append(5)
con.append(6)
con.append(7)
con.append(8)


print("after adding the new elements :", con)

#find no of occurence of 8

counts = con.count(8)

print("number of occurenence of 8:",counts)

#find average of the list

length = len(con)

avg = sum(con)//length

print("Average of the list :",avg)

#find sum of list + min ele + max ele of list

listsum = sum(con)
con.sort()

print("sum of list + min ele + max ele of list:",listsum+min(con)+max(con))

#find mean median of list



mean = listsum // length

print("Mean value is :", mean)

#median

con.sort()
median = con[len(con) // 2] 
print("median value is :",median)


#remove duplicates from concatenated list and give output in tuple format

set1 = set(con)
print("output of remove duplicates from concatenated list and give output in tuple format :", tuple(set1))



#task 2

#create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set 1
#check whether both are disjoint ?
#remove 8 from set
#discard 0 from set2
#find sum(set1 union set2)

#create two empty sets
set1 = set()
set2 = set()
print("emtpty set : ",set1)
print(type(set1))

#update set1 with 7,8,9,1,2,3,4,5,0

set1.update([7,8,9,1,2,3,4,5,0])

print("update set1 with XXX:",set1)

#update set2 with 4,5,6,0

set2.update([4,5,6,0])

#check whether set2 is subset of set 1

x = set2.issubset(set1)

print("check whether set2 is subset of set 1:", x)

#check whether both are disjoint ?


y = set1.isdisjoint(set2)

print("check whether both are disjoint:",y)

#remove 8 from set

set1.remove(8)

print("remove 8 from set:",set1)

#discard 0 from set2

set2.discard(0)

print("discard 0 from set2 :",set2)

#find sum(set1 union set2)

set3 = set1.union(set2)

sum1 = sum(set3)

print("sum of set1 union set 2 :",sum1)


#task3
#create two tuples (1,4,5,6,7) (5,6,7,8,9)
#concatenate two tuples after duplicate removal from both
#find the index value of 9
#find common elements between above elements with {0,4,5}
#multiple above tuple 3 times

#create two tuples (1,4,5,6,7) (5,6,7,8,9)

tuple1 = (1,4,5,6,7)
tuple2 = (5,6,7,8,9)

#concatenate two tuples after duplicate removal from both

set1 = set(tuple1)
set2 = set(tuple2)

set3 = set1.union(set2)

tuple3 = tuple(set3)

print("concatenate two tuples after duplicate removal from both :", tuple3)


#find the index value of 9

z = tuple3.index(9)

print("find the index value of 9:",z)

#find common elements between above elements with {0,4,5}

set4 = set3.intersection({0,4,5})
tuple4 = tuple(set4)

print("find common elements between above elements :",tuple4)

#multiple above tuple 3 times

mul = tuple4*3

print("multiple above tuple 3 times :",mul)


#task4
#create a dictionary {1:["english","maths","science":["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}
#extract botany
#extract "english","maths","science" from that dictionary and convert it into  tuple and print len
#print all keys in dictionary
#extract "python" from dictionary
#add all numbers in values under key 2 

#create a dictionary

dict1 = {1:["english","maths","science",["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}

#extract botany

print("extract botany: ",dict1[1][3][1][4:10])

#extract "english","maths","science" from that dictionary 

dict2 = dict1[1]
dict2.pop(-1)

#convert it into  tuple

tuple4 = tuple(dict2)
#print length

print("length of tuple :",len(tuple4))

#print all keys in dictionary

print("print all keys in dictionary :",dict1.keys())

#extract "python" from dictionary

print("extract from dictionary: ",dict1[2][-1][0:6])

#add all numbers in values under key 2

dict5 = dict1[2]
dict5 = list(dict5)
dict5.pop(-1)
print("add all numbers in values under key 2 :",sum(dict5))

'''






























      

