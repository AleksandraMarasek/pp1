'''8.	Identify at least 3 states and 3 behaviors for a telephone object. 
Then, for the listed states and behaviors, create a class with fields (attributes) and methods. 
Try to use verbs in method names as they describe activities. 
Finally, create a object, call its methods and display object’s properties.'''



class Phone():
    def __init__(self,brand,model,color,storage,battery,pro,used):
        self.brand=brand
        self.model=model
        self.color=color
        self.storage=storage
        self.battery=battery
        self.pro=''
        self.on=False
    def pro(self):
        if self.pro == 'yes':
            return True
        elif self.pro == 'no':
            return False
    def battery(self):
        if self.battery<=20:
            return "Your battery is low! Charge your phone!"
        elif self.battery>20 and self.battery<100:
            return "Your phone is charged"
        else:
            "Invalid battery"
    def turn_on(self):
        self.on=True
    def turn_off(self):
        self.on=False
    def __str__(self):
        return f'Your phone is from the brand {self.brand} and the model is {self.model}.\nthe color is {self.color} nd it has {self.storage} storage.'


my_phone=Phone('apple','iphone 13','white',64,74,'no','no')

print(my_phone)

print(Phone.battery(my_phone))