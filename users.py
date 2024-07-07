import csv


with open('users_languages.csv', 'r') as fh:
    reader = csv.DictReader(fh)

    Python, JS, C = 0, 0, 0

    for line in reader:
        favorite = line['Favorite Language']

        if favorite == "JS":
            JS += 1
        elif favorite == "Python":
            Python += 1
        elif favorite == "C":
            C += 1

print(f"Python: {Python}, Javascript: {JS}, C: {C}")

# Alternate method
counts = {}

# Reopen the file to reset the reader
with open('users_languages.csv', 'r') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        favorite = row['Favorite Language']
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1
print("Alternate Method:")
for favorite in sorted(counts, key=counts.get):
    print(f"{favorite}: {counts[favorite]}")
