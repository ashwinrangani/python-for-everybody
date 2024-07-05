import sqlite3

connection = sqlite3.connect('spider.sqlite')
cursor = connection.cursor()

# Find the ids that send out page rank - we only are interested
cursor.execute('SELECT DISTINCT from_id FROM Links')
from_ids = list()
for row in cursor:
    from_ids.append(row[0])

# Find the ids that receive page rank
to_ids = list()
links = list()
cursor.execute('SELECT DISTINCT from_id, to_id FROM Links')
for row in cursor:
    from_id = row[0]
    to_id = row[1]
    if from_id == to_id : continue
    if from_id not in from_ids : continue
    if to_id not in from_ids: continue
    links.append(row)
    if to_id not in to_ids: to_ids.append(to_id)

# Get latest page ranks for strongly connected component
prev_ranks = dict()
for node in from_ids:
    cursor.execute('''SELECT new_rank FROM Pages WHERE id = ?''', (node, ))
    row = cursor.fetchone()
    prev_ranks[node] = row[0]

sval = input('How many iterations: ')
many = 1
if (len(sval) > 0) : many = int(sval)

# Sanity Check
if len(prev_ranks) < 1 :
    print('Nothing to page rank.  Check data.')
    quit()

# Let's do page rank in memory so it is really fast
for i in range(many):
    # print prev_ranks.items()[:5]
    next_ranks = dict()
    total = 0.0
    for(node, old_rank) in list(prev_ranks.items()):
        total = total + old_rank
        next_ranks[node] = 0.0
    # print total

    # Find the number of outbound links and sent the page rank down each
    for (node, old_rank) in list(prev_ranks.items()):
        # print node, old_rank
        give_ids = list()
        for (from_id, to_id) in links:
            if from_id != node : continue
            if to_id not in to_ids : continue
            give_ids.append(to_id)
        if (len(give_ids) < 1): continue
        amount = old_rank / len(give_ids)
        # print node, old_rank,amount, give_ids

        for id in give_ids:
            next_ranks[id] = next_ranks[id] + amount
    
    newTotal = 0
    for(node, next_rank) in list(next_ranks.items()):
        newTotal = newTotal + next_rank
    evap = (total - newTotal) / len(next_ranks)

    # print newTotal, evap
    for node in next_ranks:
        next_ranks[node] = next_ranks[node] + evap
    
    newTotal = 0
    for (node, next_rank) in list(next_ranks.items()):
        newTotal = newTotal + next_rank

    # Compute the per-page average change from old rank to new rank
    # As indication of convergence of the algorithm
    totdiff = 0
    for (node, old_rank) in list(prev_ranks.items()):
        new_rank = next_ranks[node]
        diff = abs(old_rank - new_rank)
        totdiff = totdiff + diff
    
    avediff = totdiff / len(prev_ranks)
    print(i+1, avediff)

    # rotate
    prev_ranks = next_ranks

    # Put the final ranks back into the database
    print(list(next_ranks.items())[:5])
cursor.execute('''UPDATE Pages SET old_rank=new_rank''')
for (id, new_rank) in list(next_ranks.items()) :
    cursor.execute('''UPDATE Pages SET new_rank=? WHERE id=?''', (new_rank, id))
connection.commit()
cursor.close()

