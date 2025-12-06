"""
Builder Pattern — поетапне створення складних об'єктів.

Приклад:
    builder = WoodenHouseBuilder()
    builder.build_walls()
    builder.build_roof()
    print(builder.get_result().parts)  # ['Wooden walls', 'Wooden roof']
"""

from typing import List


class House:
    """
    Продукт — будинок, що будується.
    """

    def __init__(self) -> None:
        self.parts: List[str] = []

    def add_part(self, part: str) -> None:
        self.parts.append(part)


class HouseBuilder:
    """
    Абстрактний будівельник.
    """

    def build_walls(self) -> None:
        pass

    def build_roof(self) -> None:
        pass


class WoodenHouseBuilder(HouseBuilder):
    """
    Конкретний будівельник для дерев'яного будинку.
    """

    def __init__(self) -> None:
        self.house = House()

    def build_walls(self) -> None:
        self.house.add_part("Wooden walls")

    def build_roof(self) -> None:
        self.house.add_part("Wooden roof")

    def get_result(self) -> House:
        return self.house


if __name__ == "__main__":
    builder = WoodenHouseBuilder()
    builder.build_walls()
    builder.build_roof()
    print(builder.get_result().parts)  # ['Wooden walls', 'Wooden roof']
