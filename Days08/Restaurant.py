class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(str(self.restaurant_name))
        print(str(self.cuisine_type))

    def open_restaurant(self):
        print(str(self.restaurant_name) + ' is open')

    def set_number_served(self,numbers):
        self.number_served = numbers

    def increment_number_served(self,number2):
        self.number_served += number2

class IceCreamstand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['milk','origin','apple']

    def show_flavors(self):
        print(str(self.flavors))

restaurant = Restaurant('KFC','老八密制小汉堡')
restaurant.describe_restaurant()
restaurant.open_restaurant()
icecreamstand = IceCreamstand('kfc','none')
icecreamstand.show_flavors()
