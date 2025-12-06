"""
Facade Pattern — спрощує доступ до складної системи, надаючи єдиний інтерфейс.

Приклад:
    pc = ComputerFacade()
    print(pc.start())  # CPU started, Memory loaded, SSD read
"""


class CPU:
    def start(self) -> str:
        return "CPU started"


class Memory:
    def load(self) -> str:
        return "Memory loaded"


class SSD:
    def read(self) -> str:
        return "SSD read"


class ComputerFacade:
    """
    Simplified interface to start a complex system.
    """

    def __init__(self) -> None:
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SSD()

    def start(self) -> str:
        return f"{self.cpu.start()}, {self.memory.load()}, {self.ssd.read()}"


if __name__ == "__main__":
    pc = ComputerFacade()
    print(pc.start())  # CPU started, Memory loaded, SSD read
