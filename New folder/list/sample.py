# class Animal:
#     def speak1(self):
        
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
        

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# class Duck(Animal):
#     def speak(self):
#         return "Quack!"

# Function that takes an Animal object and calls its speak method
# def animal_sound(animal):
#     return animal.speak()
#     return animal.speak1()
# # Creating instances of different animal classes
# dog = Dog()
# cat = Cat()
# duck = Duck()

# # Calling the function with different animal objects
# print(animal_sound(dog))  # Output: Woof!
# print(animal_sound(cat))  # Output: Meow!
# print(animal_sound(duck)) # Output: Quack!
# print(speak1(dog))

# def fun():
#     a2=25
#     return a2

# import abc


# class abc:
#     x=5
#     def bcd(self):
#         self.a1=10
#         print("hai")
#     def bccd(k):
#         print("hello",k)   
# a=abc()
# a.bcd()
# print(a.x)

class Person():
   
    def __init__(self, name="John", age=30):
        # Parameterized constructor with default values
        self.nam = name
        self.ag = age

    def display_info(self):
        print("hello my name is",self.nam ,self.ag)

# Creating objects with default and custom values
person1 = Person()
person2 = Person("Alice", 25)
person2 = Person("ali",40)

# Displaying information using the display_info method
person1.display_info()
person2.display_info()
person1 = Person("alith",55)
person1.display_info()