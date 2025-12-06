"""
Singleton Pattern — гарантує наявність лише одного екземпляра класу.

Приклад:
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)  # True
"""


class Singleton:
    """
    A classic Singleton pattern implementation.

    Guarantees only one instance of the class exists.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)  # True
