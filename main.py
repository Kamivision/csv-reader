from dog import Dog
from cat import Cat

Dog.add_dogs_from_csv()
# print(Dog.available_dogs)

Cat.add_cats_from_csv()
# # print(Cat.available_cats)
# Cat.display_cats()

def user_inquiry():
    request = input("""
        Please select type of animal:
        Dog or Cat
                    """)
    request.lower()
    if request == 'cat':
        return Cat.display_cats()
    elif request == 'dog':
        return Dog.display_dogs()
    else:
        print("We only have cats and dogs please try again")
        
user_inquiry()
