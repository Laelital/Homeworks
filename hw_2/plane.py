from hw_2.exceptions import CargoOverload
from hw_2.base import Vehicle


class Plane(Vehicle):
    def __init__(self, weight, started, fuel, fuel_consumption, max_cargo: int = 0, cargo: int = 0):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self._cargo = cargo

    @property
    def cargo_space(self):
        return self.max_cargo - self.cargo

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        if value >= self.max_cargo:
            raise CargoOverload(value)
        self._cargo = value

    def load_cargo(self, value):
        if value > self.cargo_space:
            raise CargoOverload(value)
        self._cargo += value

    def remove_all_cargo(self):
        res = self._cargo
        self._cargo = 0
        return res
