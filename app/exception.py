from app.exceptions import OperationError
from decimal import Decimal, InvalidOperation

def _raise_invalid_root(x: Decimal, y: Decimal):  # pragma: no cover
    if y == 0:
        raise OperationError("Zero root is undefined")
    if x < 0:
        raise OperationError("Cannot calculate root of negative number")
    raise OperationError("Invalid root operation")


def _raise_neg_power():  # pragma: no cover
    raise OperationError("Negative exponents are not supported")

def _raise_div_zero():  # pragma: no cover
    raise OperationError("Division by zero is not allowed")