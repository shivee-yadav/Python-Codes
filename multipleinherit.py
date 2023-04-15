#multiple inheritance
class Profit:
    def getProfit(self):
        self.profit=int(input("Enter Profit: "))
    def printProfit(self):
        print("Profit:",self.profit)

class Loss:
    def getLoss(self):
        self.loss=int(input("Enter Loss: "))
    def printLoss(self):
        print("Loss:",self.loss)
        
class Balance(Profit,Loss):
    def getBalance(self):
        self.getProfit()
        self.getLoss()
        self.balance=self.profit-self.loss
    def printBalance(self):
        self.printProfit()
        self.printLoss()
        print("Balance:",self.balance)
        
user1 = Balance()
user1.getBalance()
user1.printBalance()