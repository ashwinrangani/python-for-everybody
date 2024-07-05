line = 'have a nice day'
line.startswith('h') #True
line.startswith('H') #False

#parsing and extracting using find()

text = 'From ashwin.rangani@gmail.com Sat Jan 2008'

at_pos = text.find('@')

space_pos = text.find(' ', at_pos) # Find the position of the first space after the '@' character

domain = text[at_pos+1:space_pos] # Extract the domain part

print(domain)


# Reading files
handlefile = open('py-first.py', 'r')


# for x in handlefile:
#     print(x)

count = 0
for lines in handlefile:
    count = count + 1
print("Line Count is", count) # Line count is 190

handlefile.seek(0) # Reset file pointer to the beginning of the file

for line in handlefile:
        line = line.rstrip() #remove \n lines between lines, whitespaces
        if line.startswith('str'):
            print(line)

#working with list
list = []
list.append(10)
list.append("hello")
print(list)

nums = [2,9,25,41,65,99]
length = len(nums)
maxNo = max(nums)
minNo = min(nums)
total = sum(nums)
print(length)
print(maxNo, minNo, total)
print(total/length)

#split() function

abc = "with three words"
newList = abc.split()

for words in newList:
     print(words)

xyz = "hello;my name is;xyz"
xyzList = xyz.split(";")
print(xyzList)

#Dictionaries 

dictionary = dict() # or it can be dictionary = {}

dictionary["age"] = 20
dictionary["name"] = "Ashwin"
print(dictionary)

#checking if key exists
print("age" in dictionary)
#True

#frequency distribution

counts = dict()
names = ['paresh', 'suresh', 'mahesh', 'ashwin', 'suresh']

for name in names:
     if name not in counts:
          counts[name] = 1
     else:
        counts[name] = counts[name] + 1
print(counts)
#{'paresh': 1, 'suresh': 2, 'mahesh': 1, 'ashwin': 1}

#get method
for name in names:
    y = counts.get(name, 0)
    print(y)

#simplified counting with get()

counting = dict()
listofnames = ["Alice", "Bob", "Alice", "Eve", "Bob", "Alice"]

for name in listofnames:
     counting[name] = counting.get(name, 0) + 1
print(counting)
#{'Alice': 3, 'Bob': 2, 'Eve': 1}

#Tuples

tups = ('abc', 1, 'xyz')
#tuples are immutable

#sorting list of tuples

d = {'a': 10, 'c' : 5, 'b': 20}
print(d.items()) #dict_items([('a', 10), ('c', 5), ('b', 20) ])

print(sorted(d.items())) #[('a', 10), ('b', 20), ('c', 5)]

for k ,v in sorted(d.items()):
     print(k ,v)
# a 10
# b 20
# c 5

#top 10 most common words
file = open('test.txt')
counts = dict()

for line in file:
     words = line.split()
     for word in words:
          counts[word] = counts.get(word, 0) + 1

LIST = []
for k, v in counts.items():
     newTuple = (v ,k)
     LIST.append(newTuple)
LIST = sorted(LIST, reverse=True)
for key, value in LIST[:10]:
     print(key, value)

# 9 Python
# 6 the
# 6 in
# 4 released
# 4 programming
# 4 as
# 4 and
# 4 a
# 3 was
# 3 of
     