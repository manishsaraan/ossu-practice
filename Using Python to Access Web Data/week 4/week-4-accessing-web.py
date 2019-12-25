import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

words = dict()

for line in fhand: 
    for word in line.decode().strip():
        words[word] = word

print(words)
    