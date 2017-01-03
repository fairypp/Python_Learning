``` Python
import json
import urllib


while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    ##print data
    info = json.loads(data)
    comments = info["comments"]
    print 'Count:', len(comments)
    sum = 0
    for item in comments:
        sum = sum + item['count']
    print 'Sum:', sum
```
