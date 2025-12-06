"""
Composite Pattern — створює дерево об'єктів з уніфікованим інтерфейсом.

Приклад:
    folder = Folder()
    folder.add(File("file1"))
    folder.add(File("file2"))
    print(folder.show())  # ['file1', 'file2']
"""

from typing import List


class Component:
    """
    Base component.
    """

    def show(self) -> str:
        raise NotImplementedError


class File(Component):
    def __init__(self, name: str) -> None:
        self.name = name

    def show(self) -> str:
        return self.name


class Folder(Component):
    def __init__(self) -> None:
        self.items: List[Component] = []

    def add(self, item: Component) -> None:
        self.items.append(item)

    def show(self) -> List[str]:
        return [item.show() for item in self.items]


if __name__ == "__main__":
    folder = Folder()
    folder.add(File("file1"))
    folder.add(File("file2"))
    print(folder.show())  # ['file1', 'file2']
