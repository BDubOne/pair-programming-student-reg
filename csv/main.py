import csv

class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed}."
    
class Animal_database:
    def __init__(self):
        self.data = []
    
    def open_csv_file(self, file_name):
        with open(file_name) as pet_file:
            reader = csv.DictReader(pet_file, skipinitialspace=True, delimiter=',')

            for i in reader:
                pet = Animal(i['name'], i['age'], i['breed'])
                self.data.append(pet)
                

    def find_your_pet(self, name):
        for pet in self.data:
            if pet.name == name:
                return pet
        
def call_pet():
    database = Animal_database()

    database.open_csv_file('data/dogs.csv')
    database.open_csv_file('data/cats.csv')

    while True:
        species = input("What kind of pet are you interested in? dog or cat: ")
        pet = database.find_your_pet(species)
        if pet:
            print(pet)
        else:
            print(f"Sorry, we don't have any {species}s here.")
call_pet()



# try:
    
    # animals_list = []

    # 

    # for animal in animals_list:
    #     print(animal)

# except:
    # 

    
    
# @property
# def get_name(self):
#     return self._name

# @get_name.setter
# def set_name(self, new_name):
#     if isinstance(new_name, str):
#         self.name = new_name
#     else:
#         print('Name must be a string')

# @property
# def get_age(self):
#     return self._age

# @get_age.setter
# def set_age(self, new_age):
#     if isinstance(new_age, str) and new_age > 0:
#         self._age = new_age
#     else:
#         print("")
    