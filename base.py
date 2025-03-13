from abc import ABC
from hw_2 import exceptions


class Vehicle(ABC):
    # Атрибуты класса
    weight: int
    started: bool
    fuel: int
    fuel_consumption: float

    # Метод инициализации
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0.0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    # Методы класса
    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError
        else:
            raise ValueError

    def move(self, s: int):
        if self.started:
            r = s * self.fuel_consumption / 100
            if r <= self.fuel:
                self.fuel -= r
            else:
                raise exceptions.NotEnoughFuel
        else:
            raise ValueError
