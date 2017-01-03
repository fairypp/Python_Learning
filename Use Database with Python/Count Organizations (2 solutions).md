This application will read the mailbox data (mbox.txt) count up the number email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.pythonlearn.com/code/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.pythonlearn.com/code/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.

My solutions:
Method 1

``` Python
import sqlite3
#inport the library we're going to use to talk to the SQL database


#we're going to use a database in this application
#and we're going to store that database in the file emaildb.sqllite
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
#this cursor variable now has the cursor object in it

cur.execute('''
DROP TABLE IF EXISTS Counts''')
#we have the cursor object and we call the execute method

#original code:
#cur.execute('''
#CREATE TABLE Counts (email TEXT, count INTEGER)''')

#code for assignment:
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#convert txt into table 
fname = raw_input('Enter file name: ')#file name 
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:#for lien in file handler
    if not line.startswith('From: ') : continue
    pieces = line.split('@')
    #email = pieces[1]#1 means what happens after the @
    org = pieces[1]
    org = org.rstrip() #remove blank spaces 
    #print email
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    #?means this is going to be somthing
    #(email,)is a tuple, and the 1st thing in the tuple is what will be substituted
    #for the question mark

    try:
        count = cur.fetchone()[0] #get current count
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
    except:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )

    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]
cur.close()

```

Method 2

``` Python
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute("drop table if exists Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")


name = raw_input("Enter a file name: ")
if len(name)<1: data=open("mbox-short.txt")
else: data = open(name)

pair = dict()
for line in data:
    if not line.startswith('From:'): continue
    else:
        emailfull = line.split('@')
        org = emailfull[1].rstrip()
        pair[org]=pair.get(org,0)+1

for key in pair:
    cur.execute('INSERT INTO Counts (org, count) VALUES (?,?)',(key,pair[key]))



res_table = cur.execute('SELECT * FROM Counts ORDER BY count DESC')

for item in res_table:
    print item[0], item[1]

conn.commit()

conn.close()

```
