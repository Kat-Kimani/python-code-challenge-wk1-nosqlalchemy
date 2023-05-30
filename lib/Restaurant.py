class Restaurant:
    def __init__(self, name):
        self._name=name
    def name(self):
        return self._name 
restaurant= Restaurant("Fenty")
print(restaurant.name())
   
       