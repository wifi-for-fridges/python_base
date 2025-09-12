from .base_vehicles import BaseShip
from .parts import Engine

class CargoShip(BaseShip):
    """
    A freight ship
    """

    def __init__(self, fuel_tank: int, fuel: int, *args):
        super().__init__(name=args[0], fc = args[1])
        self.FUEL_TANK = fuel_tank
        self._fuel = fuel
        self._uploaded_weight = 0
        self.engine = Engine('base ship engine')
        print(f'new ship is created: {self.__repr__()}')


    def sail(self, dist: int) -> None:
        """
        Sailing method
        :param dist: distance to sail
        :return:
        """
        res = self._fuel_spending_evaluation(dist)
        if res is None:
            return
        print(f'distance {dist} has been sailed successfully!')


    def upload(self, weight: int) -> None:
        """
        Uploading of the ship
        :param weight: weight to upload onboard
        :return:
        """
        if self._uploaded_weight == self.TONNAGE:
            print('cannot add something, the ship is fully uploaded!')
            return
        elif self.TONNAGE < weight or self.TONNAGE < self._uploaded_weight + weight:
            print('this cargo is way too heavy for that ship!')
            return

        self._uploaded_weight += weight
        print(f'the cargo has been uploaded successfully! current loading is {self._uploaded_weight}/{self.TONNAGE}')

    def unload(self, weight: int) -> None:
        """
        Unloading of the ship
        :param weight: weight to unload from the ship
        :return:
        """
        if self._uploaded_weight == 0:
            print('the ship is already empty!')
            return

        if self._uploaded_weight < weight:
            print('there is no enough cargo, but everything will be unloaded')
            self._uploaded_weight = 0
            print(f'the ship is empty!')
            return
        else:
            self._uploaded_weight -= weight
            print(f'unloaded weight: {weight}, current cargo weight is {self._uploaded_weight}')


if __name__ == '__main__':
    ship = CargoShip(10000, 3000, 'Win', 1000)
    ship.provide_sound()
    print(ship.NAME)
    ship.upload(500)
    ship.upload(1500)
    ship.upload(5000)

    ship.sail(2)
    ship.sail(3)
    ship.add_fuel(15000)
    ship.sail(10)

    ship.unload(500)
    ship.unload(2500)
    ship.unload(3000)
    ship.upload(100000)

    ship.engine.make_sound()
    ship.engine = Engine('powerful ship engine')
    ship.engine.make_sound()
