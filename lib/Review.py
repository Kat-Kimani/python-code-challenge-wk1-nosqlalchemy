from Customer import Customer
from Restaurant import Restaurant
class Review:
    all_reviews=[]
    def __init__(self, customer, restaurant, rating ):
        self._customer= customer
        self._restaurant= restaurant
        self.rating = rating
        Review.all_reviews.append(self)
    def get_rating(self):
        return self.rating
    def customer(self):
        return self._customer
    def restaurant(self):
        return self._restaurant
    @classmethod
    def get_all_reviews(cls):
        return cls.all_reviews
    
# Create customer and restaurant instances
customer = Customer("John", "Doe")
restaurant = Restaurant("The Best Restaurant")

# Create a Review instance
review = Review(customer, restaurant, 4)

# Call the rating() method and print the result
print(review.get_rating())

# Access the all_reviews list using the class method
all_reviews = Review.get_all_reviews()
print(all_reviews)  