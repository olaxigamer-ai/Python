class vehicle:
    def __init__(self, maxspeed, mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage
modelx=vehicle(240,15)

print("Model X maximum speed:",modelx.maxspeed)
print("Model X mileage:",modelx.mileage)