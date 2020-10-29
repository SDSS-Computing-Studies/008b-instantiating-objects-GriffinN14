#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""
animals = []
class pet:
    animal = None
    breed = None
    Name = None
    owner = None
    birthdate = None

    def __init__(self):
        self.animal = input("What type of animal ")
        self.breed = input("What is breed ")
        self.name = input("What is animals name ")
        self.owner = input("What is owners name ")
        self.birthdate = input ("Animals date of birth ")
            
    




# create a list of objects
# while loop until they choose to exit
# display menu and get menu choice
# if 1 - insantiate a new object and add it to the list of objects and (fill in the data)
# if 2 - ask for a name and then cycle through all of the list objects to see if the name matches and then print the name details
# if 3 then quit
while True:
    print ("===================")
    print ("1. Enter a new pet")
    print ("2. Retrive a pet")
    print ("3. Exit")
    print ("===================")
    choice = input("Enter number : ")
    if int(choice) == 1:
        animals.append(pet())
    elif int(choice) == 2:
        i = 0
        animalName = (input("Enter animals name "))
        while i != len(animals) + 1:
            if animalName == animals[i].name:
                print (animals[i].name + " " + animals[i].animal + "\n" + animals[i].breed + " is owned by " + animals[i].owner)
                break
            else:
                i = i + 1
    elif int(choice) == 3:
        print ("Good bye")
        break