import re

string = "my 2 fav numbers are 33 and 66"

# find numbers with more than one digit
print(re.findall("[0-9]+", string))

string2 = "From: Some user :"

#greedy version or find the longest pair
print(re.findall("^F.+:", string2))

#non greedy version or find the shortest pair
print(re.findall("^F.+?:", string2))

emailString = "From: someuser@somedomain.com at 5:30pm"

#greedy find non black charactes follwed by @ then more non black characters
print(re.findall("\S+@\S+", emailString))

#greedy Match the expersion but extract only in between ()
print(re.findall("^From: (\S+@\S+)", emailString))

#start from @ and return non space characters till space
print(re.findall("@([^ ]*)", emailString))

string3 = "We recieved only $10.00 for cookies"

# escape $ and match with numbers including .
print(re.findall("\$[0-9.]+", string3))