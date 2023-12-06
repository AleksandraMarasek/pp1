class Music():
    def __init__(self,artist,track,album,year):
        self.artist=artist
        self.track=track
        self.album=album
        self.year=year

    def __str__(self):
        return f'Performer:\t{self.artist}\nSong: \t\t{self.track}\nAlbum: \t\t{self.album}\nYear:\t\t{self.year}'
    
music1=Music('Lana Del Rey','A&W','Did you know that there is a tunnel under Ocean Blvd',2023)
music2=Music('The neighnourhood','Beach','xyz',1234)

print(music1)
print(music2)