#CO4 5/12/24
#2.Create a Bank account with members account number, name, type of account and balance. Write constructor and methods to #deposit at the bank and withdraw an amount from the bank.
class account:
  def __init__(self,ano,aname,atype,abalance):
    self.ano=ano
    self.aname=aname
    self.atype=atype
    self.abalance=abalance
  def deposit(self,amt):
    if amt>0:
      self.abalance=self.abalance+amt
      print("successfully deposited ",amt,"RS")
      print("your current balance now is: ",self.abalance,"RS")
    else:
      print("invalid amount")
  def withdraw(self,amt):
    if amt>self.abalance:
      print("insufficient balance")
    else:
      print("successfully withdrawn ",amt,"RS")
      self.abalance=self.abalance-amt
      print("your current balance now is: ",self.abalance,"RS")
  def viewdetails(self):
    print("Account no: ",self.ano)  
    print("Name: ",self.aname)  
    print("Account Type: ",self.atype)  
    print("Account Balance: ",self.abalance,"RS")  
ano=int(input("enter accnt no: "))
aname=input("enter name: ")
atype=input("enter accnt type: ")
abalance=int(input("enter accnt balace: "))

c1=account(ano,aname,atype,abalance)
while True:
  print("Menu\n1.Deposit\n2.Withdraw\n3.Current balance\n4.View Details\n5.Exit")
  ch=int(input("enter your choice: "))
  if ch==1:
    amt=int(input("enter amount to be deposited: "))
    c1.deposit(amt)
  elif ch==2:
    amt=int(input("enter amount to be withdrawn: "))
    c1.withdraw(amt)
  elif ch==3:
    print("current balance= ",c1.abalance,"RS")
  elif ch==4:
    c1.viewdetails()
  elif ch==5:
    break
 


 

