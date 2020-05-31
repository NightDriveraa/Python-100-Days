class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(str(self.restaurant_name))
        print(str(self.cuisine_type))

    def open_restaurant(self):
        print(str(self.restaurant_name) + ' is open')

restaurant = Restaurant('KFC','老八密制小汉堡')
restaurant.describe_restaurant()
restaurant.open_restaurant()

class User():          #类User，包含first_name 和 last_name 以及 favorite
    def __init__(self,first_name,last_name,favorite):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite = favorite

    def describe_user(self):
        print(str(self.first_name) + str(self.last_name) + ' favorite is ' + self.favorite)

    def greet_user(self):
        print('Hello ' + self.first_name + self.last_name)


user1 = User('David','Furan','football')
user2 = User('David','Huran','run')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

