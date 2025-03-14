class LowFuelError(Exception):
    """
    Исключение при топливе меньше 0
    """
    pass


class NotEnoughFuel(Exception):
    """
    Исключение при недостаточном количестве топлива
    """
    pass


class CargoOverload(Exception):
    """
    Исключение при перегрузе
    """
    pass
