def ms_to_kmh(ms):
    result=ms*3.6

    return f"{ms} m/s = {result} km/h"

m=10

if __name__=="__main__":
    print(ms_to_kmh(10))
    print(ms_to_kmh(35))