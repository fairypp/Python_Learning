```python
friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
    print 'Happy New Year:', friend

for i in range(len(friends)):
    friend = friends[i]
    print 'Happy New Year:', friend



stuff = list() #build a empty list
stuff.append('book')
stuff.append(99)
print stuff

stuff.append('cookie')
print stuff



# Is something in a List???
some = [1, 9, 21, 10, 16]
print 9 in some  #should return a 'True'
print 15 in some #should return a 'False'
print 20 not in some #should return a 'True'


#A list is an Ordered Sequence
sort method means "sort yourself"
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort() #make a change, alter the list
print friends
print friends[1]

#built in Functions and Lists
nums = [3, 41, 12, 9, 74, 15]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)


# Two ways to write summing programs
#1 if there was 10 million numbers, method 1 is better, because storing very little data 
total = 0
count = 0
while True:
    inp = raw_input('Enter a number:')
    if inp == 'done':break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print 'Average:', average

#2 if there was 10 million numbers, memory matters
numlist = list()
while True:
    inp = raw_input( 'Enter a number:')
    if inp == 'done':break
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/len(numlist)
print 'Average:', average

#Best Friends: Strings and Lists
abc = 'With three words'
stuff = abc.split()
print stuff

print len(stuff)
print stuff[0]

for w in stuff:
     print w


# A practice
line ='A lot                 of spaces'
etc = line.split()
print etc

line = 'first;second;third' #no space
thing = line.split()
print thing
print len(thing)

line = 'first; second; third'
thing = line.split('; ') #semicolon and space as a parameter to split
print thing
print len(thing)

line = 'first; second; third'
thing = line.split()# space as a parameter to split
print thing
print len(thing)

thing = line.split(';') # split on semicolon
print thing
print len(thing)

#Another sample 
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# method 1
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print words[2]
# method 2
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print words
print words[2]

#The Double Split Pattern
words = line.split()
email = words[1]
```
