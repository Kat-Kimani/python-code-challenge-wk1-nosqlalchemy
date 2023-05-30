from Review import Review
from Restaurant import Restaurant
class Customer:
    all_customers = []
    def __init__(self, given_name, family_name):
        self._given_name=given_name
        self._family_name = family_name
        Customer.all_customers.append(self)
        self._reviews = []
    def given_name(self):
        return self._given_name
    def family_name(self):
        return self._family_name
    def full_name(self):
        return f"{self.given_name()} {self.family_name()}"
    def restaurants(self):
        reviewed_restaurants = []
        for review in self._reviews:
            restaurant = review.restaurant()
            if restaurant not in reviewed_restaurants:
                reviewed_restaurants.append(restaurant)
        return reviewed_restaurants
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)
    def num_reviews(self):
        return len(self._reviews)    
    @classmethod
    def all(cls):
        return cls.all_customers
    @classmethod
    def find_by_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers():
            full_name = f"{customer.given_name()} {customer.family_name()}"
            if full_name == name:
                matching_customers.append(customer)
        return matching_customers
    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers():
            if customer.given_name() == name:
                matching_customers.append(customer)
        return matching_customers
           
# customer = Customer("George", "Washington")
# customer2 = Customer("Jane", "Smith")
# # # Print the attributes of the customer object
# print(customer.given_name())
# print(customer.family_name())
# customer._given_name = "kimani"
# print(customer.full_name())
# # Retrieve all customer instances using the `all()` method
# all_customers = Customer.all() 
# # Print the list of customer instances
# print(all_customers)

# # Print the names of the customer instances
# for customer in all_customers:
#     print(customer.full_name())

# Create customer and restaurant instances
customer = Customer("John", "Doe")
restaurant1 = Restaurant("Restaurant 1")
restaurant2 = Restaurant("Restaurant 2")
restaurant3 = Restaurant("Restaurant 3")

# Add reviews for the customer
customer.add_review(restaurant1, 4)
customer.add_review(restaurant2, 3)
customer.add_review(restaurant3, 5)
customer.add_review(restaurant1, 2)  # Adding a review for the same restaurant again

# Get the reviewed restaurants
reviewed_restaurants = customer.restaurants()

# Print the list of reviewed restaurants
for restaurant in reviewed_restaurants:
    print(restaurant.name())