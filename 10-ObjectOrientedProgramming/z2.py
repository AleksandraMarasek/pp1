'''In the TV class, add support for volume adjustment in the range 0 to 10. 
The initial value of the volume level is 0. 
Add two methods to increase and decrease the TV volume level by one. 
Note that you cannot increase or decrease the volume beyond the specified range. 
Display the current volume level in the show_status() method. 
Then check the operation of the TV by adjusting and displaying its volume level.'''

class TV():
    def __init__(self):
        self.volume=0
        self.status="off"
    def turning(self):
        if self.status=="off":
            self.status="on"
            print("your Tv is now on.")
        elif self.status=="on":
            self.status="off"
            print("your TV is now off.")
    def add_volume(self):
        if self.volume<10 and self.volume>=0:
            self.volume+=1
        elif self.volume==10:
            print("you cannot increase your TV volume anymore.")

    def subtract_volume(self):
        if self.volume>=1 and self.volume<=10:
            self.volume-=1
        elif self.volume==0:
            print("you cannot decrease your TV volume anymore")

    def __str__(self):
        return f"TV Status: {self.status}, Volume: {self.volume}"

tv1=TV()

tv1.add_volume()
tv1.add_volume()

print(tv1)