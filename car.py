from hw_2.base import Vehicle
from hw_2.engine import Engine


class Car(Vehicle):
    engine: Engine = None

    def __init__(self, engine: Engine, weight, started, fuel, fuel_consumption):
        self.engine = engine
        super().__init__(weight, started, fuel, fuel_consumption)

    def set_engine(self, engine: Engine):
        self.engine = engine
