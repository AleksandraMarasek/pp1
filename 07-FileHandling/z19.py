meatfish='meatandfish.txt'
grainsbread='grainsandbread.txt'

all='allproducts.txt'

with open(meatfish, 'r') as meatfish1:
    meatfish2=meatfish1.read()

with open(grainsbread, 'r') as grainsbread1:
    grainsbread2=grainsbread1.read()

with open(all, 'w') as all1:
    all1.write(meatfish2)
    all1.write('\n')
    all1.write(grainsbread2)


grainsbread1.close()
meatfish1.close()
all1.close()
