## 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.
class Restaurant:
    def _init_(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
# Create an instance of the Restaurant class
restaurant = Restaurant("The Italian Kitchen", "Italian")

# Print the restaurant name and cuisine type attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call the describe_restaurant() and open_restaurant() methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

## Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each instance.
def _init_(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
        
def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
 # Create three instances of the Restaurant class
restaurant1 = Restaurant("The Italian Kitchen", "Italian")
restaurant2 = Restaurant("Taco Time", "Mexican")
restaurant3 = Restaurant("Indian Palace", "Indian")

# Call the describe_restaurant() method for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

## 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.
class User:
    def _init_(self, first_name, last_name, age, city, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
    
    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.city}, {self.country}")
        # add more attributes as needed
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")
# Create several instances of the User class
user1 = User("John", "Musa", 25, "New York", "USA")
user2 = User("Alice", "Smith", 32, "London", "UK")
user3 = User("Bob", "Jones", 45, "Toronto", "Canada")

# Call the describe_user and greet_user methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

## 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
#day of business.
class Restaurant:
    def _init_(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number
restaurant = Restaurant("La Trattoria", "Italian")
print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 10
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(20)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(15)
print(f"Number of customers served: {restaurant.number_served}")

## 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
#_attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempt to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.
class User:
    def _init_(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome to our website.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
user1 = User("John", "Musa", 35, "Male", "Software Engineer")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Login attempts: {user1.login_attempts}")

user1.reset_login_attempts()

print(f"Login attempts: {user1.login_attempts}")

## 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.
class Restaurant:
    def _init_(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    def _init_(self, restaurant_name, cuisine_type="ice cream"):
        super()._init_(restaurant_name, cuisine_type)
        self.flavors = []
    
    def display_flavors(self):
        print("We have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor)

## 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.
class User:
    def _init_(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.age}-year-old {self.gender}.")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def _init_(self, first_name, last_name, age, gender):
        super()._init_(first_name, last_name, age, gender)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print(f"{self.first_name} has the following privileges:")
        for privilege in self.privileges:
            print("- " + privilege)

## 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges
class User:
    def _init_(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.age}-year-old {self.gender}.")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def _init_(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print(f"The administrator has the following privileges:")
        for privilege in self.privileges:
            print("- " + privilege)


class Admin(User):
    def _init_(self, first_name, last_name, age, gender):
        super()._init_(first_name, last_name, age, gender)
        self.privileges = Privileges()
    
    def show_privileges(self):
        self.privileges.show_privileges()

## 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 100 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def _init_(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery capacity to 100 kWh if it is not already."""
        if self.battery_size < 100:
            self.battery_size = 100

        from electric_car import ElectricCar

        my_car = ElectricCar('Tesla', 'Model S', 2019)
        my_car.battery.get_range()

        my_car.battery.upgrade_battery()
        my_car.battery.get_range()

