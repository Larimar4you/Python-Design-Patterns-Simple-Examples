"""
Observer Pattern — дозволяє об'єкту повідомляти інші об'єкти про зміни свого стану.

Приклад:
    subject = Subject()
    listener = Listener()
    subject.attach(listener)
    subject.notify("Event fired!")  # Received: Event fired!
"""

from typing import List, Protocol


class Observer(Protocol):
    def update(self, data: str) -> None: ...


class Subject:
    """
    Notifies observers about changes.
    """

    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify(self, data: str) -> None:
        for observer in self._observers:
            observer.update(data)


class Listener:
    def update(self, data: str) -> None:
        print(f"Received: {data}")


if __name__ == "__main__":
    subject = Subject()
    listener = Listener()
    subject.attach(listener)
    subject.notify("Event fired!")  # Received: Event fired!
