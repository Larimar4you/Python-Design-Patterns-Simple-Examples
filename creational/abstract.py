"""
Abstract Factory Pattern — створює родини пов'язаних об'єктів без прив'язки до конкретних класів.

Приклад:
    factory = ModernFactory()
    chair = factory.create_chair()
    print(chair.sit())  # Sitting on modern chair
"""

from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def sit(self) -> str:
        pass


class ModernChair(Chair):
    def sit(self) -> str:
        return "Sitting on modern chair"


class VictorianChair(Chair):
    def sit(self) -> str:
        return "Sitting on victorian chair"


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass


class ModernFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()


class VictorianFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()


if __name__ == "__main__":
    factory = ModernFactory()
    chair = factory.create_chair()
    print(chair.sit())  # Sitting on modern chair
