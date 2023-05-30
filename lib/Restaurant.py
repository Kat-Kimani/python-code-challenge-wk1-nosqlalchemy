class Restaurant:
    def __init__(self, name):
        self._name=name
        self._reviews=[]
    def name(self):
        return self._name
    def reviews(self):
        return self._reviews
    def customers(self):
        customer_list=set()
        for review in self._reviews:
            customer_list.add(review.customer())
        return list(customer_list)
        
restaurant= Restaurant("Fenty")
print(restaurant.name())
   
       