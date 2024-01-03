'''Create a class that describes cell phones with at least 3 phone states and 2 behaviors. 
Define a text representation of an object. 
Then, create 2 objects. 
Display their features and call their bahaviors.
'''

class phone():
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.state = 'off'

    def phone_turning(self):
        if self.state=="off":
            self.state="on"
            print(f"{self.brand} {self.model} is now on")
        elif self.state=="on":
            self.state="off"
            print(f"{self.brand} {self.model} is now off")
        elif self.state=="calling":
            print("You cannot turn your phone off while on call")
        
    def call(self, contact):
        if self.state=="on":
            self.state="calling"
            print(f"calling {contact}...")
        elif self.state == 'off':
            print(f"Cannot make a call while the phone is off. Power it on first.")
        elif self.state=="calling":
            print(f"you can't make another call.")

    def __str__(self):
        return f"The phone is {self.brand} {self.model} in color {self.color} - state: {self.state}"

phone1= phone("Iphone","13","pink")
phone1.phone_turning()
phone1.call("piwo")
phone1.phone_turning()

print(phone1)