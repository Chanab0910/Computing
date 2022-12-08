class Bank:
    next_account_number = 10_000

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}
        self.transactions = []

    def __repr__(self):
        return f"Bank('{self.bank_name}')"

    def add_account(self, ac_password, amount=0):
        Bank.next_account_number += 1
        self.accounts[Bank.next_account_number] = \
            BankAccount(Bank.next_account_number, ac_password, amount)
        return Bank.next_account_number

    def check_account_number(self, ac_number):
        return ac_number in self.accounts.keys()

    def transact(self, source_account, dest_account, amount, transaction_datetime=datetime.now()):
        if amount <= 0:
            raise TransactionError("Transaction must be for a positive amount")
        if source_account.get_balance() < amount:
            raise TransactionError("Insufficient funds in source account")
        source_account.transfer(dest_account, amount)
        self.transactions.append({
            "date": transaction_datetime,
            "source_acc": source_account.account_number,
            "destination_acc": dest_account.account_number,
            "amount": amount,
        })
