from .base_vehicles import BaseCar
from .parts import Engine

class Car(BaseCar):
    """
    Normal passenger car
    """
    def __init__(self, fuel_tank: int, fuel:int, *args):
        super().__init__(*args)
        self.FUEL_TANK = fuel_tank
        self._fuel = fuel
        self.engine = Engine()
        print(f'new car created: {self.__repr__()}')


    def drive(self, dist: int) -> None:
        """
        Driving method
        :param dist: distance to drive
        :return:
        """
        res = self._fuel_spending_evaluation(dist)
        if res is None:
            return
        print(f'distance {dist} has been driven successfully!')


if __name__ == '__main__':
    car = Car(100, 60,'mazda', 'beep', 10, 250, 1500)
    car.provide_sound()
    print(car.MODEL)

    car.drive(5)
    car.drive(3)
    car.add_fuel(5000)

    car.add_fuel(40)
    car.add_fuel(40)
    car.drive(10)
    car.drive(5)

    car.engine.make_sound()
    car.engine = Engine('sport engine')
    car.engine.make_sound()
