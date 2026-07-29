class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount 
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            balance -= amount
    def transfer(self, other_acct, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            other_acct.balance += amount

angie_acct = BankAccount("Angie", 1234)
kai_acct = BankAccount("Kai", 5678)

angie_acct.withdraw(2000)
angie_acct.deposit(2000)
print(angie_acct.balance)

angie_acct.transfer(kai_acct, 2500)
angie_acct.transfer(kai_acct, 1500)

print(angie_acct.balance)
print(kai_acct.balance)


# nums = 0
# for i in range(5000,7501):
#     if(i % 3 == 0 or i % 5 == 0 and not(i % 15 == 0)):
#         nums+= 1
# print(nums)

sum = 0
stringfs = "I <3 Python!"
for i in range(len(stringfs)):
    sum += ord(stringfs[i])
print(sum)

nums = 0
for i in range (10,13):
    curr = i
    currSum = 0
    while (curr > 0):
        currSum += (curr%10)
        curr /= 10
    print(currSum)
    if (currSum % 2 == 1):
        nums += 1
print(nums)
        