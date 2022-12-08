class BankAccount:
    def __init__(self, balance, acc_num):
        self.balance = balance
        self.acc_num = acc_num

    def credit(self, value):
        self.balance += value

    def debit(self,value):
        self.balance -= value

    def show_balance(self):
        print(f'Balance is {self.balance}')

    def show_acc_num(self):
        print(f'Your account number is {self.acc_num}')

    def transer(self, account, value):
        self.debit(value)
        account.credit(value)



