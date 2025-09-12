from .base_vehicles import BasePlane
from .parts import Engine

class Jet(BasePlane):
    """
    A small plane
    """
    def __init__(self,fuel_tank: int, fuel: int, *args):
        super().__init__(model=args[0])
        self.FUEL_TANK = fuel_tank
        self._fuel = fuel
        self.engine = Engine('base plane engine')
        print(f'new plane is created: {self.__repr__()}')


    def fly(self, dist: int) -> None:
        """
        Flying method
        :param dist: distance to fly
        :return:
        """
        res = self._fuel_spending_evaluation(dist)
        if res is None:
            return
        print(f'distance {dist} has been flown successfully!')


if __name__ == '__main__':
    jet = Jet(5000, 1000, 'jet')
    jet.provide_sound()
    print(jet.MODEL)

    jet.fly(0.5)
    jet.fly(1)
    jet.add_fuel(50000)
    jet.add_fuel(40)
    jet.add_fuel(40)

    jet.engine.make_sound()
    jet.engine = Engine('jet engine')
    jet.engine.make_sound()
