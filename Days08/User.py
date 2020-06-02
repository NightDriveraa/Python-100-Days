class User():          #类User，包含first_name 和 last_name 以及 favorite
    def __init__(self,first_name,last_name,favorite):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite = favorite
        self.login_attempts = 0

    def describe_user(self):
        print(str(self.first_name) + str(self.last_name) + ' favorite is ' + self.favorite)

    def greet_user(self):
        print('Hello ' + self.first_name + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print('Admin\'s privileges: ')
        for privileges in self.privileges:
            print(str(privileges))

class Admin(User):
    def __init__(self,first_name,last_name,favorite):
        super().__init__(first_name,last_name,favorite)
        self.privileges = Privileges()


user1 = User('David','Furan','football')
user2 = User('David','Huran','run')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user1.increment_login_attempts()
print(str(user1.login_attempts))
user1.reset_login_attempts()
print(str(user1.login_attempts))
admin = Admin('ws','z','eat')
admin.privileges.show_privileges()
