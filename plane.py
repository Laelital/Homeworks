from hw_2.exceptions import CargoOverload
from hw_2.base import Vehicle


class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, max_cargo=0, cargo=0, weight=0, started=False, fuel=0, fuel_consumption=0.0):
        self.max_cargo = max_cargo
        self.cargo = cargo
        super().__init__(weight, started, fuel, fuel_consumption)

    def load_cargo(self, n):
        if n + self.cargo > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += n

    def remove_all_cargo(self):
        res = self.cargo
        self.cargo = 0
        return res
