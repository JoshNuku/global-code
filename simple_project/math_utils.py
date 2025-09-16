"""Small math utility functions with simple, well-documented behavior."""

from typing import Iterable


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean of a non-empty iterable of numbers.

    Raises:
        ValueError: if values is empty.
    """
    vals = list(values)
    if not vals:
        raise ValueError("mean() arg is an empty iterable")
    return sum(vals) / len(vals)
