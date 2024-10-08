import xml.etree.ElementTree as ET
import sqlite3

connection = sqlite3.connect('trackdb.sqlite')
cursor = connection.cursor()

cursor.executescript(
    '''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);
CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

'''
)

fname = input('Enter File Name: ')
if (len(fname) < 1) : fname = 'Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count', len(all))
for entry in all:
    if(lookup(entry, 'Track ID') is None): continue
    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    count = lookup(entry, "Play Count")
    rating = lookup(entry, "Rating")
    length = lookup(entry, "Total Time")

    if name is None or artist is None or album is None:
        continue
    print(name, artist, album, count, rating, length)

    cursor.execute(''' INSERT OR IGNORE INTO Artist (name)
             VALUES( ? ) ''', (artist, ))
    cursor.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cursor.fetchone()[0]

    cursor.execute(''' INSERT OR IGNORE INTO Album (title, artist_id)
             VALUES( ?, ? ) ''', (album, artist_id ))
    cursor.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cursor.fetchone()[0]

    cursor.execute(
        '''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count) 
        VALUES (?, ?, ?, ?, ?)''',
        (name, album_id, length, rating, count)
    )
    connection.commit()
