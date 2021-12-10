class atm:
    def __init__(self,atmCard, atmPin, balance):
        self.atmCard = atmCard
        self.atmPin = atmPin
        self.balance = balance
    def Cashwithdrawl(self,amount):
        self.balance = self.balance - amount
        print("Your remaining balance is:")
        print(self.balance)
    def Cashdeposit(self,amount):
        self.balance = self.balance + amount
        print("Your remaining balance is:")
        print(self.balance)
        
def main():
    card = input("Pls enter your card No.")
    pin = input("Pls enter your pin No.")
    balance = int(input("Pls enter your account balance"))
    user = atm(card, pin, balance)
    choice = int(input("To withdraw the amount enter 1; To deposit the amount enter 2"))
    amount = int(input("Pls enter the amount to be deposited or withdrawn"))
    if(choice==1):
        user.Cashwithdrawl(amount)
    elif(choice==2):
        user.Cashdeposit(amount)
    else:
        print("Invalid number.")

main()