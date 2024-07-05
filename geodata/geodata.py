import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys
api_key = False # if we have api key, enter it here

if api_key is False:
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
else:
    serviceurl = "https://maps.googleapis.com/maps/place/textsearch/json?"

connection = sqlite3.connect("geodata.sqlite")
cursor = connection.cursor()

cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)
'''
)
#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("geodata\where.data")
count = 0
for line in fh:
    if count > 200:
        print("Retrieved 200 locations, restart to retrieve more")
    address= line.strip()
    print('')
    cursor.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cursor.execute()[0]
        print("found in database", address)
        continue
    except:
        pass

    params = dict()
    params["query"] = address
    if api_key is not False: params["key"] = api_key
    url = serviceurl + urllib.parse.urlencode(params)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("Retrieved", len(data), 'characters', data[:20].replace('\n', ''))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)
        continue
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print("====Failure to Retrieve")
        print(data)
        break
    cursor.execute('''INSERT INTO Locations (address, geodata) VALUES(?, ?)''', (memoryview(address.encode()), memoryview(data.encode())))
    connection.commit()
    if count % 10 == 0:
        print('Pausing for a bit...')
        time.sleep(5)
print("Run geodump.py to read the data from the database so you can visualize on map")