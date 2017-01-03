``` Python
# Fine-Tuning String Extraction
#\S+@\S+
#\S+ \S+ means at least one non-whitespace character
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
y = re.findall('\S+@\S+',x) 
print y
#['stephen.marquard@uct.ac.za']
#find out the things that match this particular regular expression'\S+@\S+'
#in this particular string and low and behold and we get a list
#findall always gives us back a list that gives us exactly what we want


y = re.findall('^From (\S+@\S+)',x)
print y
#['stephen.marquard@uct.ac.za']
#find a LINE first 5 characters from the followed by a blank
#()means the start and the end of what to extract
#look for non-blank character, at least one followed by an @ sign 
#followed by one or more non-blank character and then stop matching



data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print atpos
#21
sppos = data.find(' ',atpos) #find the next space after the @ sign
print sppos
#31
host = data[atpos+1 : sppos] #don't include the sppos
print host
#uct.ac.za


# The Double Split Pattern
words = line.split() #split based on spaces

email = words[1]
#stephen.marquard@uct.ac.za

pieces = email.split('@') # another split based on @ sign
#['stephen.marquard', 'uct.ac.za']

print pieces[1]
#'uct.ac.za'


# The Regex Version
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
#@ : look through the string untile you fine an at sign
#[^ ]: Match non-blank character 
# * : Match many of them
print y
#['uct.ac.za']


#Even Cooler Regex Version
y=re.findall('^From .*@([^ ]*)',lin)#From at the beginning of the line
# insist on a space
#then on any number of characters untile find an @ sign
#then we start extracting 
#and keep going extracting as long as they're non-blank
#then we hit a blank, then we stop extracting
print y
#['uct.ac.za']


# Spam Confidence
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
line = line.rstrip()
stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) #[0-9.] means digital or dot
if len(stuff) != 1 : continue
num = float(stuff[0])
numlist.append(num)
print 'Maximum:', max(numlist)
python ds.py
X-DSPAM-Confidence: 0.8475

# Escape Character
#If you want a special regular expression character to just
#behave normally (most of the time) you prefix it with '\'
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print y
#['$10.00']
#\$ : A real dollar sign
#[0-9.]: A digit or period
# + : At least one or more





```
