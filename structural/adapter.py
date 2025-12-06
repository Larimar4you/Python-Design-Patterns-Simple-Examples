"""
Adapter Pattern — адаптер для несумісних інтерфейсів.

Приклад:
    usa = USASocket()
    adapter = Adapter(usa)
    print(adapter.plug_in())  # 110V
"""

from typing import Protocol


class EuropeanSocket(Protocol):
    """
    Інтерфейс для європейських розеток.
    """

    def plug_in(self) -> str: ...


class USASocket:
    """
    Пристрій з інтерфейсом, несумісним з європейським.
    """

    def plug_110(self) -> str:
        return "110V"


class Adapter:
    """
    Адаптер перетворює інтерфейс USASocket на EuropeanSocket.
    """

    def __init__(self, device: USASocket) -> None:
        self.device = device

    def plug_in(self) -> str:
        return self.device.plug_110()


if __name__ == "__main__":
    usa = USASocket()
    adapter = Adapter(usa)
    print(adapter.plug_in())  # 110V
