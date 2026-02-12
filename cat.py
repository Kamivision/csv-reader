import csv
class Cat: 
    available_cats = []
    
    def __init__(self, name, age, breed):
        self.name = name 
        self.age = age
        self.breed = breed
    
    @classmethod
    def add_cats_from_csv(cls, relative_path = './data/cats.csv'):
        with open(relative_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cleaned_row = {key.strip(): value for key, value in row.items()}
                cls.create_cat(cleaned_row)
    
    @classmethod
    def create_cat(cls, cat_dict):
        try:
            new_cat = cls(**cat_dict)
            print(f"{new_cat.name} has been added")
            cls.available_cats.append(new_cat)
            return new_cat
        except Exception as e:
            print(e, cat_dict)
            return None
    # @staticmethod
    # def retrieve_cats(available_cats):
        
    
    @classmethod
    def display_cats(cls):
        print("""
                Here's Our List of Cats
                -----------------------
                """)
        for cat in cls.available_cats:
             print(cat)
        
    
    @classmethod
    def create_cat_from_user(cls):
        user_data = {
            "name":input("Please provide a name:\n"), 
            "age":input("What is the cats age?\n"), 
            "breed": input("Please provide the cats breed:\n")
        }
        cls.create_cat_(user_data)
               

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
        return f"{self.name} is a {self.age} year old {self.breed}\n"
    
    # def __repr__(self):
    #     return f"class Cat: {self.name}"