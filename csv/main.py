import csv

species = input("What kind of pet are you interested in? dog or cat: ")

try:
    with open(f'./data/{species.lower()}s.csv') as csv_file:
        reader_csv_file = csv.DictReader(csv_file)

        for i in reader_csv_file:
            print(i)
except:
    print(f"Sorry, we don't have any {species}s here.")

class Animal:
    def __init__(self, name, age, breed):
        self._name = name
        self._age = age
        self._breed = breed
    
    def __str__(self):
        return f"{self._name} is a {self._age} year old {self._breed}"
    
    
@property
def get_name(self):
    return self._name

@get_name.setter
def set_name(self, new_name):
    if isinstance(new_name, str):
        self.name = new_name
    else:
        print('Name must be a string')

@property
def get_age(self):
    return self._age

@get_age.setter
def set_age(self, new_age):
    if isinstance(new_age, str) and new_age > 0:
        self._age = new_age
    else:
        print("")
    