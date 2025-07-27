def greet(name):
    print(f"Hello {name}\nHow are you?\nHow's whether today?")

name = input("What's Your Name: ")
greet(name)



# Functions with input

def greet_with_name(name,location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"How's Whether In {location}")

name = input("Enter Your Name: ")
location = input("Enter Your Location: ")
greet_with_name(name,location)
