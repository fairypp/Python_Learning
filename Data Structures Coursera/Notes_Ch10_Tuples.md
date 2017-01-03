``` Python
#Tuples are another kind of sequence that function much like a list
#they have elements which are indexed starting at 0

x = ('Gleen', 'Sally', 'Joseph')
print x[2]
#Joseph

y = (1, 9, 2)
print y
#(1, 9, 2)
print max(y)
#9

for iter in y:
    print iter
#1
#9
#2

# Tuples are "immutable"
#Unlike a list, once you create a tuple, you cannot alter its contents- similar to a string

x = [9, 8, 7]  #list
x[2] = 6
print x
#[9, 8, 6]

y = 'ABC'  #String
y[2] = 'D'
#Traceback :
# 'str' object does not support item assignment

z = (5, 4, 3) # Tuples
z[2] = 0
#Traceback :
# 'str' object does not support item assignment

# Things not to do with tuples
x = (3, 2, 1)
x.sort()
x.append(5)
x.reverse()
#Traceback :
# 'tuple' object has no attribute 'sort', 'append', 'reverse'

# A Tale of Two Sequences
l = list()
#dir(l)
print dir(l)
#['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

t = tuple()
#dir(t) #what can we do with tuple
print dir(t)
#['count', 'index']

# Tuples are more efficient
# So we prefer tuples over lists when we are making "temporary variables"


#Tuples and Assignment
#We can also put a tuple on the left hand side of an assignment statement
#We can even omit the parenthesis

(x, y) = (4, 'fred')
print y
#fred

a, b = (99, 98)
print a
#99

# Tuples and Dictionaries
# The items() method in dictionaries returns a list of (key, value) tuples

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print k, v


tups = d.items()
print tups

# Tuples are Comparable
# The comparison operators work with tuples and other sequences
# If the first item is equal, Python goes on to the next element, and so on
(0, 1, 2) < (5, 1, 2)
#True
(0, 1, 2000000) < (0, 3, 4)
#True
('Jones', 'Sally') < ('Jones', 'Fred')
#False
('Jones', 'Sally') > ('Adams', 'Sam')
#True


# Sorting Lists of Tuples
# First we sort the dictionary by the key using the items() method
d = {'a':10, 'b':1, 'c':22}
t = d.items()
t
print t
#[('a', 10), ('c', 22), ('b', 1)]

t.sort()
t
print t
#[('a', 10), ('b', 1), ('c', 22)]


# Using sorted() 
# We can do this even more directly using the built-in function sorted 
# that takes a sequence as a parameter and returns a sorted sequence
d = {'a':10, 'b':1, 'c':22}
d.items()
print d.items()
#[('a', 10), ('c', 22), ('b', 1)]

t = sorted(d.items())
print t
#[('a', 10), ('b', 1), ('c', 22)]


for k, v in sorted(d.items()):
    print k, v
#a 10
#b 1
#c 22

# Sort by values instead of key
# If we could construct a list of tuples of the form (value,key) we could sort by value
# We do this with a for loop that creates a list of tuples
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )#make a two_tuple with values from the v and K variable
                        #and append a list

print tmp
#[(10, 'a'), (22, 'c'), (1, 'b')]
#each of the tuples now has the value first and the key second
#they a in a list


tmp.sort(reverse=True)# List is mutable 
print tmp
#[(22, 'c'), (10, 'a'), (1, 'b')]
#a list in new order

# Top 10 most common words
fhand = open('romeo.txt')#open a file
counts = dict ()#create a empty counts dictionary
for line in fhand:#write a for loop that reads each line for line in fhand
    words = line.split()#split each line into words, based on the splace
    for word in words:#loop each word in each line
        counts[word] = counts.get(word, 0) + 1
        #If the word key exists, give me back the value that's in that, otherwise give me zero
        #create the new entries and update old entries

#we are going to have counts with keyword word-count pairs
lst = list()
for key, val in counts.items():
    lst.append((val, key)) #create temporary list of tuples that are val, comma, key

lst.sort(reverse=Ture) #the biggest value will near the top

for val, key in lst[:10]: #first 10 items
    print key, val



# Even Shorter Version(adv)
c = {'a':10, 'b':1, 'c':22} #a dictionary
print sorted([(v,k) for k,v in c.items()])
#[(1, 'b'), (10, 'a'), (22,'c')]
#List comprehension creates a dynamic list. In this case, 
#we make a list of reversed tuples and then sort it
#http://wiki.python.org/moin/HowTo/Sorting

#[(v,k) for k,v in c.items()] construct dynamically a list of tuples v, comma, k
#loop through the items with k and v taking on the successive values
#(v,k) is creating a reversed list where value and key are the order of the items in each tuple

#pass it to sort, this is a function call    
#print out its ascending order of the value









```
