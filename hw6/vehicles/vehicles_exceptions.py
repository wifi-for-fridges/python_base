class NoFuelException(ValueError):
    def __str__(self):
        print('there is no fuel at all')


class NotEnoughFuelException(ValueError):
    def __init__(self, cur_fuel, reqr_fuel):
        self.fuel = cur_fuel
        self.required = reqr_fuel


    def __str__(self):
        print(f'not enough fuel! you have {self.fuel} but {self.required} is needed!')
