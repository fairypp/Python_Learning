```python
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print purse
print purse['candy']
purse['candy'] = purse['candy'] + 2
print purse
#{'money': 12, 'tissues': 75, 'candy': 3}
#3
#{'money': 12, 'tissues': 75, 'candy': 5}


# Dictionary Literals (Constants)
jjj = {'chuck':1, 'fred':42, 'jan':100}
print jjj
ooo = {} #can be empty
print ooo
#{'jan': 100, 'chuck': 1, 'fred': 42}
#{}

# When we see a new name
counts = dict()
names = ['csev','cwen','csev','zqian','cwen','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print counts
#{'csev': 2, 'zqian': 1, 'cwen': 3}
#3
#3

# The get method for dictionary
if name in counts:
    print counts[name]
else:
    print 0


print counts.get(name, 0)
#{'csev': 2, 'zqian': 1, 'cwen': 2}




# Simplified counting with get()
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print counts


# Counting Pattern
counts = dict()
print 'Enter a line of text:'
line = raw_input('')

words = line.split() # the split takes a string and prodeces a list
                    # So the words is a list,line is a string 
print 'Words:', words

print 'Counting...'
for word in words:
    counts[word] = counts.get(word,0) + 1

print 'Counts', counts

#Enter a line of text:
#s a s w d a d s q d 
#Words: ['s', 'a', 's', 'w', 'd', 'a', 'd', 's', 'q', 'd']
#Counting...
#Counts {'a': 2, 'q': 1, 's': 3, 'd': 3, 'w': 1}


# Definite Loops and Dictionaries
counts = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts:
    print key, counts[key]
#jan 100
#chuck 1
#fred 42


# Retrieving lists of Keys and Values
# You can get a list of keys, values or items (both) from a dictionary
jjj = {'chuck':1, 'fred':42, 'jan':100}
print list(jjj)
#['jan', 'chuck', 'fred']
print jjj.keys()
#['jan', 'chuck', 'fred']
print jjj.values()
#[100, 1, 42]
print jjj.items()
#[('jan', 100), ('chuck', 1), ('fred', 42)]


#Bonus: Two Iteration Variables
#Each iteration, the 1st variable is the key and the 2nd variable is the corresponding value for the key
jjj = {'chuck':1, 'fred':42, 'jan':100}
for aaa, bbb in jjj.items():
    print aaa, bbb

#jan 100
#chuck 1
#fred 42

# all the way back to the beginning
name = raw_input("Enter file:") #ask for a file name
handle = open(name, 'r')#open the file for read
text = handle.read()#read the whole file, newlines and all and put it in the variable called text
words = text.split()#go through the whole string, which was the whole file, go through and split it all
#It throws the newlines away and the blanks away, and split it into a beautiful list of just words with no      blanks
#And the list of the words in that file ends up in the variable words
#text is a string, words is a list

#now pattern of accumulating counters in a dictionary
counts = dict() #make an empty dictionary
for word in words: #have the word variable that goes through all the words 
    counts[word] = counts.get(word,0) + 1 #count sub word equals counts dot get(word,0) + 1
#at the point in the program, we have a full dictionary with the word:count


#a largest loop, find the largest
bigcount = None#set the largest count we've seen so far to None
bigword = None#set the largest word we've seen so far to None
for word,count in counts.items(): #use this two-iteration variable pattern to say go through the   key/value pairs word and count in count.items
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword,bigcount

#python words.py
#Enter file: words.txt
#to 16

#python words.py
#Enter file:clown.txt
#the 7
```
