class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage

class bus(vehicle):
    pass

schoolbus=bus('School Honda',200, 10)
print("Vehicle name is",schoolbus.name)
print("Vehicle top speed is", schoolbus.maxspeed)
print("Vehicle mileage is",schoolbus.mileage)
