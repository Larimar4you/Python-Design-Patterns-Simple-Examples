"""
State Pattern — дозволяє об'єкту змінювати поведінку при зміні його стану.

Приклад:
    switch = Switch()
    print(switch.click())  # Light OFF
    switch.set_state(On())
    print(switch.click())  # Light ON
"""

from abc import ABC, abstractmethod


class State(ABC):
    """
    Базовий інтерфейс стану.
    """

    @abstractmethod
    def handle(self) -> str:
        pass


class On(State):
    """Конкретний стан — увімкнений."""

    def handle(self) -> str:
        return "Light ON"


class Off(State):
    """Конкретний стан — вимкнений."""

    def handle(self) -> str:
        return "Light OFF"


class Switch:
    """
    Контекст — керує станом і змінює поведінку об'єкта.
    """

    def __init__(self) -> None:
        self.state: State = Off()

    def set_state(self, state: State) -> None:
        """
        Змінює стан об'єкта.
        """
        self.state = state

    def click(self) -> str:
        """
        Виконує поведінку відповідно до поточного стану.
        """
        return self.state.handle()


if __name__ == "__main__":
    switch = Switch()
    print(switch.click())  # Light OFF
    switch.set_state(On())
    print(switch.click())  # Light ON
