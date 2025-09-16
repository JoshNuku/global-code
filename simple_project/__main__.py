"""Make simple_project runnable as a script: python -m simple_project"""

from . import math_utils


def _demo():
    print("simple_project demo")
    print("add(2,3) ->", math_utils.add(2, 3))
    print("multiply(3,4) ->", math_utils.multiply(3, 4))
    print("mean([1,2,3]) ->", math_utils.mean([1, 2, 3]))


if __name__ == "__main__":
    _demo()
