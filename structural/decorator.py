"""
Decorator Pattern — динамічне розширення функціоналу об'єкта або функції.

Приклад:
    @make_bold
    def hello() -> str:
        return "Hello"
    print(hello())  # <b>Hello</b>
"""

from typing import Callable


def make_bold(func: Callable[[], str]) -> Callable[[], str]:
    """
    Decorator adds <b> HTML tag to text.
    """

    def wrapper() -> str:
        return f"<b>{func()}</b>"

    return wrapper


@make_bold
def hello() -> str:
    return "Hello"


if __name__ == "__main__":
    print(hello())  # <b>Hello</b>
