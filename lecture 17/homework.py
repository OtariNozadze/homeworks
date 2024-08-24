from multipledispatch import dispatch 

class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan
    
    def __str__(self):
        return f"Person(name={self.name}, deposit={self.deposit}, loan={self.loan})"
    
    def update_deposit(self, amount):
        self.deposit += amount

    def update_loan(self, amount):
        self.loan += amount


class House:
    def __init__(self, ID, price, owner, status="To be sold"):
        self.ID = ID
        self.price = price
        self.status = status
        self.owner = owner
    
    @dispatch(Person)
    def sell_house(self, buyer):
        if self.status == "To be sold":
            self.owner.update_deposit(self.price)
            self.status = "Sold"
            self.owner = buyer
         
    
    @dispatch(Person, int)
    def sell_house(self, buyer, loan):
        if self.status == "To be sold":
            self.owner.update_deposit(self.price)
            self.owner = buyer
            buyer.update_loan(loan)
            self.status = "Sold With Loan"
    
    def __str__(self):
        return f"House(ID={self.ID}, price=${self.price}, status={self.status}, owner={self.owner})"
          
        
        

buyer_person = Person("jhon")
print(buyer_person)
owner_person = Person("Kate")
house = House(123456, 7000, owner_person)

print(house)

house.sell_house(buyer_person, 9000)

print(house)

print(owner_person)
        



        

    
    

        
