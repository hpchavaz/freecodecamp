sTransferTo = "Transfer to"
sTransferFrom = "Transfer from"

class Category:
  
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0.0
  

  def deposit(self, amount, description=""):
    self.ledger.append({'amount' : amount, 'description' : description})
    self.balance += amount

  
  def withdraw(self, amount, description=""):
    if self.balance < amount:
      return False
    
    self.ledger.append({'amount' : - amount, 'description' : description})
    self.balance -= amount

    return True
  
  
  def get_balance(self):
    return self.balance

  
  def transfer(self, amount, category):
    if not(self.withdraw(amount, sTransferTo + " " + category.name)):
      return False
    
    category.deposit(amount, sTransferFrom + " "+ self.name)

    return True

  
  def check_funds(self,check):
    return  not( check > self.balance)
    

  def __str__(self):
    s = "*" * ((30-len(self.name)) // 2) + self.name + "*" * (((30-len(self.name)) //2)+1)
    s = s[0:30] +'\n'
    for entry in self.ledger:
      s += f"{entry['description'][0:23]:23}{entry['amount']:>7.2f}" + '\n'
    s += f"Total: {self.balance:.2f}"
    return s



def create_spend_chart(categories):
  if len(categories)>4: return
  
  spents = []
  spent = 0
  maxlenname = 0
  for category in categories:
    spentcat = 0
    for entry in category.ledger:
      if (entry['amount'] < 0) & (entry['description'][0:len(sTransferTo)] != sTransferTo):
        spentcat -= entry['amount']
    spents.append({'name' : category.name, 'spent': spentcat})
    spent += spentcat
    maxlenname = max(maxlenname, len(category.name))
  for cat in spents:
    cat['percent'] = cat['spent'] / spent * 100
  
  sret = "Percentage spent by category" + '\n'
  for floor in range(100,-1,-10):
    sret += f"{floor:>3}|"
    for cat in spents:
      val = cat['percent']
      if val ==  0.0 : val = -1
      sret += "   " if (floor >= val) else " o "
    sret += " \n"
  sret += ' ' * 4 + "-" * (3 * len(spents) + 1) + '\n'
  
  for i in range(0,maxlenname):
    sret += ' ' * (4 - 1)
    for cat in spents:
      sret += "  " + (cat['name'][i] if (len(cat['name'])> i) else " ")
    sret += "  \n"
  
  sret = sret[:-1]

  return sret