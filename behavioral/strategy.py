"""
Strategy Pattern — дозволяє змінювати алгоритми на льоту, не змінюючи клас контексту.

Приклад:
    ctx = Context(Add())
    print(ctx.run(2, 3))  # 5
    ctx.set_strategy(Multiply())
    print(ctx.run(2, 3))  # 6
"""

from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Base interface for interchangeable algorithms.
    """

    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass


class Add(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a + b


class Multiply(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a * b


class Context:
    """
    Context selects which strategy to apply.
    """

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def run(self, a: int, b: int) -> int:
        return self.strategy.execute(a, b)


if __name__ == "__main__":
    ctx = Context(Add())
    print(ctx.run(2, 3))  # 5
    ctx = Context(Multiply())
    print(ctx.run(2, 3))  # 6
