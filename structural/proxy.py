"""
Proxy Pattern — контролює доступ до об'єкта, часто для оптимізації або обмеження доступу.

Приклад:
    proxy = ImageProxy()
    print(proxy.display())  # Displaying image
"""


class RealImage:
    def display(self) -> str:
        return "Displaying image"


class ImageProxy:
    """
    Proxy controls creation of heavy RealImage object.
    """

    def __init__(self) -> None:
        self.image: RealImage | None = None

    def display(self) -> str:
        if self.image is None:
            self.image = RealImage()
        return self.image.display()


if __name__ == "__main__":
    proxy = ImageProxy()
    print(proxy.display())  # Displaying image
