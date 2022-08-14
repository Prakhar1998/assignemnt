class FuelStation:

    def __init__(self, diesel: int, petrol: int, electric: int):
        self.diesel = diesel
        self.petrol = petrol
        self.electric = electric
        self.diesel_ = diesel
        self.petrol_ = petrol
        self.electric_ = electric

    def fuel_vehicle(self, fuel_type: str) -> bool:
        if fuel_type == 'petrol':
            if self.petrol > 0:
                self.petrol -= 1
                return True
            else:
                return False
        elif fuel_type == 'diesel':
            if self.diesel > 0:
                self.diesel -= 1
                return True
            else:
                return False
        else:
            if fuel_type == 'electric':
                self.electric -= 1
                return True
            else:
                return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        if fuel_type == 'petrol':
            if self.petrol < self.petrol_:
                self.petrol += 1
                return True
            else:
                return False
        elif fuel_type == 'diesel':
            if self.diesel < self.diesel_:
                self.diesel += 1
                return True
            else:
                return False
        else:
            if self.electric < self.electric_:
                self.electric += 1
                return True
            else:
                return False


fuel_station = FuelStation(2, 2, 1)
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.fuel_vehicle('petrol'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.fuel_vehicle("electric"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("diesel"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("electric"))
print(fuel_station.open_fuel_slot("electric"))