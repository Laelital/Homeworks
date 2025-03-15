from hw_2.base import Vehicle
from hw_2.engine import Engine


class Car(Vehicle):
     def __init__(self, weight, started, fuel, fuel_consumption, engine: Engine = None):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine: Engine):
        self.engine = engine
