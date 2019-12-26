import xml.etree.ElementTree as ET
data = '''
 <users>
  <persons>
    <person>
     <name>Manish</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
    </person>
     <person>
     <name>Manish</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
    </person>
  </persons>
 </users>
'''

users = ET.fromstring(data)
persons = users.findall("persons/person")

for user in persons:
    print("Name:-", user.find("name").text)
