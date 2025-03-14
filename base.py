from abc import ABC
from hw_2 import exceptions


class Vehicle(ABC):
    # Атрибуты класса
    weight: int = 0
    started: bool = False
    fuel: int = 0
    fuel_consumption: float = 0.0

    def __init__(self, weight, started, fuel, fuel_consumption):
        self.weight = weight
        self._started = started
        self._fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self._started:
            raise ValueError
        if self._fuel <= 0:
            raise exceptions.LowFuelError
        self._started = True

    def move(self, s: int):
        if self._started:
            r = s * self.fuel_consumption / 100
            if r <= self.fuel:
                self.fuel -= r
            else:
                raise exceptions.NotEnoughFuel
        else:
            raise ValueError

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
