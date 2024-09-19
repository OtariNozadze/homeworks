import unittest
from bank import BankAccount
class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank_owner1 = BankAccount("Jhon")
        self.bank_owner2 = BankAccount("Kate", 2000)
        self.bank_owner3 = BankAccount("Jane", -200)
    
    def test_get_balance(self):
        self.assertEqual(self.bank_owner1.get_balance(), 0)
        self.assertEqual(self.bank_owner2.get_balance(), 2000)
        self.assertEqual(self.bank_owner3.get_balance(), -200)
    
    def test_deposit(self):
        with self.assertRaises(ValueError) as context:
            self.bank_owner1.deposit(0)
        self.assertEqual(str(context.exception), "Deposit amount must be positive")

        with self.assertRaises(ValueError) as context:
            self.bank_owner2.deposit(-100)
        self.assertEqual(str(context.exception), "Deposit amount must be positive")

        self.bank_owner1.deposit(3000)
        self.bank_owner2.deposit(2000)
        self.bank_owner3.deposit(300)
        self.assertEqual(self.bank_owner1.balance, 3000)
        self.assertEqual(self.bank_owner2.balance, 4000)
        self.assertEqual(self.bank_owner3.balance, 100)

    def test_withcraw(self):
        test_cases = [
        (self.bank_owner1, 1000),
        (self.bank_owner2, 4000),
        (self.bank_owner3, 100)
        ]
    
        for owner, amount in test_cases:
            with self.assertRaises(ValueError) as context:
                owner.withdraw(amount)
            self.assertEqual(str(context.exception), "Insufficient funds")

        self.bank_owner2.withdraw(1000)
        self.assertEqual(self.bank_owner2.balance, 1000)

    
    
if __name__ == "__main__":
    unittest.main()