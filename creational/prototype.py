"""
Prototype Pattern — клонування об'єктів без прямого створення нових екземплярів.

Приклад:
    circle = Shape("red")
    circle_clone = circle.clone()
    print(circle.color, circle_clone.color)  # red red
    print(circle is circle_clone)            # False
"""

import copy


class Prototype:
    """
    Base class providing clone method using deepcopy.
    """

    def clone(self) -> "Prototype":
        return copy.deepcopy(self)


class Shape(Prototype):
    """
    Example concrete prototype with a color attribute.
    """

    def __init__(self, color: str) -> None:
        self.color = color


if __name__ == "__main__":
    circle = Shape("red")
    circle2 = circle.clone()

    print(circle.color, circle2.color)  # red red
    print(circle is circle2)  # False
