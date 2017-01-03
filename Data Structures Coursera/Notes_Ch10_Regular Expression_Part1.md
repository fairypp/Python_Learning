``` Python
# ^
# Using re.search() like find()
hand = open('mbox-short.txt') #open file
for line in hand: #loop through the file
    line = line.rstrip() #take away the sufix, the blanks at the end
    if line.find('From:') >= 0:
    #if line.startswith('From:')
    #check to see if the line
    #we are using the find to say does this line have the string "From:" in it?
    #the position is line.find, and if the position is >=0, away we go
        print line



import re #import the regular expression library

hand = open('mbox-short.txt') #open the file
for line in hand: #loop through the file
    line = line.rstrip() #strip the characters at the end 
    if re.search('^From:', line):
    #re.search is going to return us a true or false 
    #and it has an regular expression
    #find, look through this line here, and find the string 'From:'
    #if it's there, get a true, if it's not, you get a false
    #Dear regular expression, look through this line and find out if you find 
    #the string From at the beginning  
        print line

#loop through the file, 
#printing out the lines that have the string "From:" in them somewhere     




#Wild-Card character
#The dot character matches any character
#If you add the asterisk character, the character is "any number of times"

#^X.*:
#^ caret means beginning of line
#. dot means any character
#* star means as needed
#a number of these lines will match

#X-Sieve: CMU Sieve 2.3
#X-DSPAM-Result: Innocent
#X-DSPAM-Confidence: 0.8475
#X-Content-Type-Message-Body: text/plain


# Fine-Tuning Your Matching
# ^X-\S+:
# ^ : Match the start of the line
# + : One or more times
# \S: Match any non-whitespace character
# For example:
#X-Sieve: CMU Sieve 2.3
#X-DSPAM-Result: Innocent
#X-Plane is behind schedule: two weeks



#Matching and Extracting Data
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) #[0-9]+ means one or more digits
print y
#['2', '19', '42']
y = re.findall('[AEIOU]+',x)
print y
#[]


# Warning: Greedy Matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y
#['From: Using the :']

#^F: First character in the match is an F
#.+: One or more characters
#: : Last character in the match is a :


# None-Greedy Matching
import re
x = 'From: Using the: haha : character'
y = re.findall('^F.+?:', x)
print y
# ['From:']
# ? says don't do the Greedy matching

```
