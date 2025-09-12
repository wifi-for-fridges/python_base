from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Union
from .vehicles_exceptions import NoFuelException, NotEnoughFuelException


@dataclass
class BaseVehicle:
    """
    Base for means of transport
    """

    WEIGHT: int
    SOUND: str
    FUEL_CONSUMPTION: int
    TONNAGE: int
    FUEL_TANK: int
    _fuel: int

    def provide_sound(self) -> None:
        """
        Just making sound of the vehicle
        :return:
        """
        print(f'making sound: {self.SOUND}')


    def _fuel_spending_evaluation(self, dist: int) -> Union[int, None]:
        """
        The base method for moving forward, evaluates the required amount of fuel
        :param dist: distance to go
        :return:
        """
        if self._fuel == 0:
            try:
                raise NoFuelException
            except NoFuelException as nfe:
                nfe.__str__()
            return

        fuel_to_spend = dist * self.FUEL_CONSUMPTION
        if self._fuel < fuel_to_spend:
            try:
                raise NotEnoughFuelException(self._fuel, fuel_to_spend)
            except NotEnoughFuelException as nefe:
                nefe.__str__()
            return
        self._fuel -= fuel_to_spend
        return 0


    def add_fuel(self, fuel: int) -> None:
        """
        Refueling method
        :param fuel: amount to add
        :return:
        """
        if self._fuel == self.FUEL_TANK:
            print('there is no free space in the tank')
            return
        if self.FUEL_TANK < fuel:
            print(f'way too fuel for this tank ({self.FUEL_TANK}), a less amount will be added')
        self._fuel += fuel
        if self.FUEL_TANK < self._fuel:
            self._fuel -= self._fuel - self.FUEL_TANK
        print(f'refueled, the current amount is {self._fuel}')


class BaseCar(BaseVehicle, metaclass=ABCMeta):
    """
    Base for cars
    """

    def __init__(
            self,
            model: str,
            sound: str = 'beep!',
            fc: int = 15,
            tonnage: int = 200,
            weight: int = 1000,
            wheels: int = 4
    ):
        self.MODEL = model
        self.SOUND = sound
        self.FUEL_CONSUMPTION = fc
        self.TONNAGE = tonnage
        self.WEIGHT = weight
        self.WHEELS_NUMBER = wheels

    @abstractmethod
    def drive(self, dist: int):
        pass


class BaseShip(BaseVehicle, metaclass=ABCMeta):
    """
    Base for ships
    """

    def __init__(
            self,
            name: str = 'my_ship',
            sound: str = "horn's sound",
            fc: int = 0,
            tonnage: int = 5000,
            weight: int = 50000
    ):
        self.NAME = name
        self.SOUND = sound
        self.FUEL_CONSUMPTION = fc
        self.TONNAGE = tonnage
        self.WEIGHT = weight

    @abstractmethod
    def sail(self, dist: int):
        pass


class BasePlane(BaseVehicle, metaclass=ABCMeta):
    """
    Base for planes
    """

    def __init__(
            self,
            model: str,
            sound: str = 'noise sound',
            fc: int = 500,
            tonnage: int = 0,
            weight: int = 20000
    ):
        self.MODEL = model
        self.SOUND = sound
        self.FUEL_CONSUMPTION = fc
        self.TONNAGE = tonnage
        self.WEIGHT = weight

    @abstractmethod
    def fly(self, dist: int):
        pass
