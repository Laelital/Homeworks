from abc import ABC
from hw_2 import exceptions


class Vehicle(ABC):
       def __init__(self, weight: int = 0, started: bool = False, fuel: int = 0, fuel_consumption: float = 0.0):
        self.weight = weight
        self._started = started
        self._fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self._started:
            raise ValueError('Нельзя запустить двигатель повторно')
        if self._fuel <= 0:
            raise exceptions.LowFuelError(self._fuel)
        self._started = True

    def move(self, distance: int):
        if self._started:
            total_fuel = distance * self.fuel_consumption / 100
            if total_fuel <= self.fuel:
                self.fuel -= total_fuel
            else:
                raise exceptions.NotEnoughFuel(distance)
        else:
            raise ValueError('Сначала нужно запустить двигатель')


    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        self._fuel = value

    @property
    def started(self):
        return self._started

    @started.setter
    def started(self, value):
        self._started = value
