import sqlite3

connection = sqlite3.connect('spider.sqlite')
cursor = connection.cursor()

print('Creating JSON output on spider.js')
howmany = int(input("How many nodes? "))

cursor.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
    FROM Pages JOIN Links ON Pages.id = Links.to_id
    WHERE html IS NOT NULL AND ERROR IS NULL
    GROUP BY id ORDER BY id,inbound''')

fh = open('pagerank\spider.js', 'w' )
nodes = list()
maxrank = None
minrank = None
for row in cursor:
    nodes.append(row)
    rank = row[2]
    if maxrank is None or maxrank < rank : maxrank = rank
    if minrank is None or minrank > rank : minrank = rank
    if len(nodes) > howmany : break

if maxrank == minrank or maxrank is None or minrank is None:
    print('Error - please run sprank.py to compute page rank')
    quit()

fh.write('spiderJson = {"nodes":[\n')
count = 0
map = dict()
ranks = dict()
for row in nodes :
    if count > 0 : fh.write(',\n')
    # print row
    rank = row[2]
    rank = 19 * ( (rank - minrank) / (maxrank - minrank) )
    fh.write('{'+'"weight":'+str(row[0])+',"rank":'+str(rank)+',')
    fh.write(' "id":'+str(row[3])+', "url":"'+row[4]+'"}')
    map[row[3]] = count
    ranks[row[3]] = rank
    count = count + 1
fh.write('],\n')

cursor.execute('SELECT DISTINCT from_id, to_id FROM Links')
fh.write('"links":[\n')

count = 0
for row in cursor :
    # print row
    if row[0] not in map or row[1] not in map : continue
    if count > 0 : fh.write(',\n')
    rank = ranks[row[0]]
    srank = 19 * ( (rank - minrank) / (maxrank - minrank) ) 
    fh.write('{"source":'+str(map[row[0]])+',"target":'+str(map[row[1]])+',"value":3}')
    count = count + 1
fh.write(']};')
fh.close()
cursor.close()

print("Open force.html in a browser to view the visualization")
