"""
Iterator Pattern — забезпечує послідовний доступ до елементів колекції без
розкриття її внутрішньої структури.

Приклад:
    it = Iterator([1, 2, 3])
    for number in it:
        print(number)  # 1 2 3
"""

from typing import List, Iterator as TypingIterator


class Iterator(TypingIterator[int]):
    """
    Simple iterator over list.
    """

    def __init__(self, items: List[int]) -> None:
        self.items = items
        self.index = 0

    def __next__(self) -> int:
        if self.index < len(self.items):
            value = self.items[self.index]
            self.index += 1
            return value
        raise StopIteration


if __name__ == "__main__":
    it = Iterator([1, 2, 3])
    for number in it:
        print(number)  # 1 2 3
