"""
Factory Method Pattern — створює об'єкти без вказівки конкретного класу.

Приклад:
    vehicle = TransportFactory.create("car")
    print(vehicle.move())  # Driving
"""

from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Abstract base class for transport objects.
    """

    @abstractmethod
    def move(self) -> str:
        pass


class Car(Transport):
    def move(self) -> str:
        return "Driving"


class Bike(Transport):
    def move(self) -> str:
        return "Cycling"


class TransportFactory:
    """
    Factory that creates transport based on a string identifier.
    """

    @staticmethod
    def create(kind: str) -> Transport:
        if kind == "car":
            return Car()
        if kind == "bike":
            return Bike()
        raise ValueError(f"Unknown transport type: {kind}")


if __name__ == "__main__":
    vehicle = TransportFactory.create("car")
    print(vehicle.move())  # Driving
