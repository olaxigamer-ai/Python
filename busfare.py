class Vehicle:
    def __init__(self, seat_capacity):
        self.seat_capacity = seat_capacity
    def fare(self):
        return self.seat_capacity * 100
    
class Bus(Vehicle):
    def fare(self):
        base_fare= super().fare()
        maintenance_charge=base_fare*0.10
        total_fare=base_fare + maintenance_charge
        return total_fare
bus = Bus(50)
print("The total bus Far is : ", bus.fare())