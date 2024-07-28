class Category:
    def __init__(self,categories):
        self.categories = categories
        self.ledger = [] 

    def deposit(self,amount,description=''):
        obj = {'amount': amount,'description': description}
        self.ledger.append(obj)
    
    def withdraw(self, amount,description=''):
        current = 0
        for transaction in self.ledger:
            current += transaction['amount']
        if amount <= current:
            obj = {'amount': -amount,'description': description}
            self.ledger.append(obj)
            return True
        else:
            return False
    
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.categories}"):
            category.deposit(amount, f"Transfer from {self.categories}")
            return True
        else:
            return False

    def check_funds(self,amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def __str__(self):
    
        title = f"{self.categories:*^30}\n"

        item_list = ''
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            item_list += f"{item['description'][:23]:23}{amount:>7}\n"

            total = f"Total: {self.get_balance():.2f}"
        return title + item_list + total




def create_spend_chart(categories):
  output = "Percentage spent by category\n"

  # Retrieve total expense of each category
  total      = 0
  expenses   = []
  labels     = []
  len_labels = 0

  for item in categories:
    expense    = sum([-x['amount'] for x in item.ledger if x['amount'] < 0])
    total     += expense

    if len(item.categories) > len_labels:
      len_labels = len(item.categories)

    expenses.append(expense)
    labels.append(item.categories)

  # Convert to percent + pad labels
  expenses = [(x/total)*100 for x in expenses]
  labels   = [categories.ljust(len_labels, " ") for categories in labels]

  # Format output
  for c in range(100,-1,-10):
    output += str(c).rjust(3, " ") + '|'
    for x in expenses:
      output += " o " if x >= c else "   "
    output += " \n"

  # Add each category name
  output += "    " + "---"*len(categories) + "-\n"

  for i in range(len_labels):
    output += "    "
    for label in labels:
      output += " " + label[i] + " "
    output += " \n"

  return output.strip("\n")

food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([food,entertainment,business]))

