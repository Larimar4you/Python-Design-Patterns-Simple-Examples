"""
Command Pattern — інкапсулює запит у вигляді об'єкта, дозволяючи
зберігати, передавати та виконувати команди.

Приклад:
    invoker = Invoker(PrintCommand())
    print(invoker.run())  # Printed!
"""

from abc import ABC, abstractmethod


class Command(ABC):
    """
    Wraps an action in an object.
    """

    @abstractmethod
    def execute(self) -> str:
        pass


class PrintCommand(Command):
    def execute(self) -> str:
        return "Printed!"


class Invoker:
    """
    Executes stored command.
    """

    def __init__(self, command: Command) -> None:
        self.command = command

    def run(self) -> str:
        return self.command.execute()


if __name__ == "__main__":
    invoker = Invoker(PrintCommand())
    print(invoker.run())  # Printed!
