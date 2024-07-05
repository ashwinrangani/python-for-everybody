a = True

if a:
    print('a is true')
else:
    print('a is not true')

# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

width = 20
height = 5 * 2
print(width * height)

print(" 'yes', they said")

a , b = 0, 1

while a < 10:
    print(a, end=',')
    a , b = b, a+b


x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('More')

#for loop
words = ['cat', 'window', 'doorstep']

for w in words:
    print(w, len(w))

#loop over a copy of the collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# 1. Iterating over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# 2. Create a new Collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(active_users)


# the range() function => generate arithmatic progression

for i in range(5):              
    print(i)

#range(stop) range(start, stop) range(start, stop, step) step=difference in a.p.
list(range(5)) #[0,1,2,3,4]
list(range(5, 10)) #[5,6,7,8,9]
list(range(0, 10, 3)) #[0, 3, 6, 9]
list(range(-10, -100, -30)) #[-10, -40, -70]
 #iterating over indices of a sequence, combine range() and len()

list = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(list)):
    print (i, list[i])

# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb
sum(range(4)) # 0 + 1 + 2 + 3 = 6

# break and continue Statements, and Clauses on Loops
# The break statement breaks out of the innermost enclosing for or while loop.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x) # // floor division, get quotient without decimal 
            break
    else:
        print(n, 'is a prime number')

# The continue statement, continues with the next iteration of the loop
for num in range(2, 10):
    if num % 2 == 0:
        print('Found an even number', num)
        continue
    print('"Found an odd number', num)
""" 
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
"""

# pass Statements => The pass statement does nothing.


class MyEmptyClass:
    pass #This is commonly used for creating minimal classes

def initlog(*args):
    pass  # Remember to implement this!

# match Statements : A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.
def http_error(status):
    match status:
        case 400:
            return 'Bad Request'
        case 404:
            return 'Not Found'
        case 200 | 2001:
            return 'Status ok'
        case 418:
            return 'Im a teapot'
        

#point in an (x, y) tuple (Tuples are used to store multiple items in a single variable.)
def coordinate(point):
    match point:
        case (0 ,0):
            print("Origin")
        case (0 ,y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case(x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")


coordinate((0, 0)) # Origin

#find the largest number
largest_so_far = -1
for number in [5,7,9,12,15]:
    if number > largest_so_far:
        largest_so_far = number
print(largest_so_far)

#find the smallest
smallest = None  # Initialize smallest to None

for number in [5, 7, 9, 12, 15]:
    if smallest is None:  # Check if smallest is still None (first iteration)
        smallest = number
    elif number < smallest:  # Check if the current number is smaller than the current smallest
        smallest = number

print(smallest)  # Print the smallest number found


#upper and lower case
word = 'Hello'
toUpper = word.upper()
print(toUpper)

another_word = 'HELLO'
toLower = another_word.lower()
print(toLower)

#search and replace

string = 'Hello you'
changed = string.replace('you', 'Me')
print(changed)

#stripping whitespace

str = ' hello bob '
str.lstrip() #'hello bob '
str.rstrip() #' hello bob'
str.strip() #'hello bob'

