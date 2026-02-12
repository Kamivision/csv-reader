import csv
class Dog: 
    available_dogs = []
    
    def __init__(self, name, age, breed):
        self.name = name 
        self.age = age
        self.breed = breed
    
    @classmethod
    def add_dogs_from_csv(cls, relative_path = './data/dogs.csv'):
        with open(relative_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cleaned_row = {key.strip(): value for key, value in row.items()}
                cls.create_dog(cleaned_row)
    
    @classmethod
    def create_dog(cls, dog_dict):
        try:
            new_dog = cls(**dog_dict)
            print(f"{new_dog.name} has been added")
            cls.available_dogs.append(new_dog)
            return new_dog
        except Exception as e:
            print(e, dog_dict)
            return None
    
    @classmethod
    def create_dog_from_user(cls):
        data_dict = {
            "name":input("Please provide a name:\n"), 
            "age":input("What is the dogs age?\n"), 
            "breed": input("Please provide the dogs breed:\n")
        }
        cls.create_dog_instance(data_dict)
               

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_val):
        if isinstance(name_val, str):
            self._name = name_val.strip().title()
        else:
            raise Exception("A name should be a `str` value")
    
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed}"
    
    def __repr__(self):
        return f"class Dog: {self.name}"
