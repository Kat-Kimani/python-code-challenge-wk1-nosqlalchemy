class Customer:
    all_customers = []
    def __init__(self, given_name, family_name):
        self._given_name=given_name
        self._family_name = family_name
        Customer.all_customers.append(self)
    def given_name(self):
        return self._given_name
    def family_name(self):
        return self._family_name
    def full_name(self):
        return f"{self.given_name()} {self.family_name()}"
    @classmethod
    def all(cls):
        return cls.all_customers        
customer = Customer("George", "Washington")
customer2 = Customer("Jane", "Smith")
# # Print the attributes of the customer object
print(customer.given_name())
print(customer.family_name())
customer._given_name = "kimani"
print(customer.full_name())
# Retrieve all customer instances using the `all()` method
all_customers = Customer.all() 
# Print the list of customer instances
print(all_customers)

# Print the names of the customer instances
for customer in all_customers:
    print(customer.full_name())