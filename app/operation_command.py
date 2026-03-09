from abc import abstractmethod, ABC
from decimal import Decimal, InvalidOperation

from app.exception import _raise_invalid_root, _raise_neg_power, _raise_div_zero

class Command(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AddCommand(Command):
    def execute(self, a, b):
        return Decimal(a + b)


class SubtractCommand(Command):
    def execute(self, a, b):
        return Decimal(a - b)


class MultiplyCommand(Command):
    def execute(self, a, b):
        return Decimal(a * b)

class DivisionCommand(Command):
    def execute(self, a, b):
        if b == 0:
            raise _raise_div_zero()
        return Decimal(a / b)

class PowerCommand(Command):
    def execute(self, a, b):
        if b < 0:
            raise _raise_neg_power()
        return Decimal(pow(float(a), float(b)))

class RootCommand(Command):
    def execute(self, a, b):
        if a >= 0 and b != 0:
            return Decimal(pow(float(a), 1 / float(b)))
        else:
            raise _raise_invalid_root(a, b)

class ModulusCommand(Command):
    def execute(self, a, b):
        if b == 0:
            raise _raise_div_zero()
        return Decimal(a % b)


class IntegerDivisionCommand(Command):
    def execute(self, a, b):
        if b == 0:
            raise _raise_div_zero()
        return Decimal(a // b)

class PercentageCommand(Command):
    def execute(self, a, b):
        if b == 0:
            raise _raise_div_zero()
        return Decimal(a / b) * 100


class AbsoluteDifferenceCommand(Command):
    def execute(self, a, b):
        return Decimal(abs(a - b))
