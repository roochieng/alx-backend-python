#!/usr/bin/env python3
"""
module to perform complicated multiplication
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make multiplier
    """
    def multiply(multiple: float) -> float:
        """
        multiple
        """
        return float(multiplier * multiple)

    return multiply
