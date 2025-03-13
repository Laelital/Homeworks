class LowFuelError(Exception):
    """
    Исключение при топливе меньше 0
    """
    def __init__(self, message='Количество топлива меньше нуля'):
        self.message = message


class NotEnoughFuel(Exception):
    """
    Исключение при недостаточном количестве топлива
    """
    def __init__(self, message='Недостаточное количество топлива для данного расстояния'):
        self.message = message


class CargoOverload(Exception):
    """
    Исключение при перегрузе
    """
    def __init__(self, message='Перегруз'):
        self.message = message

