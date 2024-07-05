import xml.etree.ElementTree as ET

data = '''
<person>
<name>Ashwin</name>
<phone type='intl'>9180005465</phone>
<email hide='yes'/>
</person>
'''
tree = ET.fromstring(data)
print('name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))