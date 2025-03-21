class LowFuelError(Exception):
    """
    Исключение при топливе = 0
    """
    def __init__(self, value, message='Количество топлива'):
        self.value = value
        self.message = message
        super().__init__(self, message)

    def __str__(self):
        return f'{self.message}: {self.value}'


class NotEnoughFuel(Exception):
    """
    Исключение при недостаточном количестве топлива
    """
    def __init__(self, value, message='Недостаточно топлива для расстояния'):
        self.value = value
        self.message = message
        super().__init__(self, message)

    def __str__(self):
        return f'{self.message} = {self.value}'


class CargoOverload(Exception):
    """
    Исключение при перегрузе
    """
    def __init__(self, value, message='Перегруз при добавлении'):
        self.value = value
        self.message = message
        super().__init__(self, message)

    def __str__(self):
        return f'{self.message}: {self.value}'
