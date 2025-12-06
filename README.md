# Python-Design-Patterns-Simple-Examples

Ласкаво просимо! 👋
Тут зібрані найзрозуміліші, акуратні та практичні приклади основних патернів проектування на Python. Все лаконічно, по суті і без нудоти — щоб ти могла легко і швидко застосовувати патерни на практиці.

---

## 🚀 Цілі репозиторію

- Показати _прості та мінімалістичні_ приклади кожного патерну
- Надати структуру, яку можна одразу використовувати у реальних проектах
- Сформувати "muscle memory" Python-патернів

---

## 📂 Структура проекту

```
Python-Design-Patterns-Simple-Examples/
│
├── behavioral/        # Поведінкові патерни
│   ├── command.py
│   ├── iterator.py
│   ├── observer.py
│   ├── state.py
│   └── strategy.py
│
├── creational/        # Порождаючі патерни
│   ├── abstract.py
│   ├── builder.py
│   ├── factory.py
│   ├── prototype.py
│   └── singleton.py
│
├── structural/        # Структурні патерни
│   ├── adapter.py
│   ├── composite.py
│   ├── decorator.py
│   ├── facade.py
│   └── proxy.py
│
│
└── README.md          # Цей файл
```

---

📌 Таблиця застосування паттернів (текстова версія)

• Поведінкові паттерни:

Strategy → Динамічна заміна алгоритму без зміни класу → Реальний кейс: Алгоритми сортування, обчислення податків

Observer → Повідомлення багатьох об’єктів про зміни стану → Реальний кейс: UI підписка на події, системи сповіщень

Command → Інкапсуляція дій у вигляді об’єкта, зберігання та виконання → Реальний кейс: Undo/Redo, запуск завдань у черзі

State → Зміна поведінки об'єкта при зміні стану → Реальний кейс: Клас Switch, ігрові стани персонажів

Iterator → Послідовний доступ до елементів без розкриття структури → Реальний кейс: Перебір елементів списків, деревоподібних структур

• Порождаючі паттерни:

Singleton → Один екземпляр об'єкта для всього додатку → Реальний кейс: Логер, конфігурація

Factory → Створення об'єктів без залежності від класу → Реальний кейс: Створення різних транспортних засобів

Abstract Factory → Створення сімейств взаємопов’язаних об’єктів → Реальний кейс: UI теми (Dark/Light) з різними компонентами

Builder → Поетапне створення складних об'єктів → Реальний кейс: Конструктор HTML форм, генерація документів

Prototype → Клонування об'єктів без створення нового → Реальний кейс: Копіювання налаштувань користувача

• Структурні паттерни:

Adapter → Несумісні інтерфейси робимо сумісними → Реальний кейс: Підключення пристрою з іншою напругою

Facade → Спрощений інтерфейс до складної системи → Реальний кейс: Клас ComputerFacade для старту комп'ютера

Decorator → Динамічне розширення поведінки без зміни класу → Реальний кейс: HTML-рендеринг, логування функцій

Proxy → Контроль доступу або оптимізація ресурсів → Реальний кейс: Віртуальні об’єкти, lazy loading зображень

Composite → Робота з деревоподібними структурами об’єктів → Реальний кейс: Файлова система, UI компоненти

## 🧠 Поведінкові патерни (Behavioral)

### **Strategy — заміна алгоритмів на льоту**

```python
class Strategy:
    def execute(self, a, b):
        pass

class Add(Strategy):
    def execute(self, a, b):
        return a + b

class Multiply(Strategy):
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def run(self, a, b):
        return self.strategy.execute(a, b)

ctx = Context(Add())
ctx.run(2, 3)  # 5
```

---

## 🧱 Порождаючі патерни (Creational)

### **Singleton — один об'єкт на всю програму**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

---

### **Factory Method — фабрика для створення об'єктів**

```python
class Transport:
    def move(self):
        pass

class Car(Transport):
    def move(self):
        return "Driving"

class Bike(Transport):
    def move(self):
        return "Cycling"

class TransportFactory:
    @staticmethod
    def create(kind):
        if kind == "car":
            return Car()
        if kind == "bike":
            return Bike()
```

---

## 🧩 Структурні патерни (Structural)

### **Adapter — адаптер несумісних інтерфейсів**

```python
class EuropeanSocket:
    def plug_in(self):
        return "220V"

class USASocket:
    def plug_110(self):
        return "110V"

class Adapter:
    def __init__(self, device):
        self.device = device

    def plug_in(self):
        return self.device.plug_110()
```

---

### **Decorator — динамічне розширення функціоналу**

```python
def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

@make_bold
def hello():
    return "Hello"
```

---

## 🌟 Як використовувати цей репозиторій

- Відкривай будь-який файл — всередині окремий мінімальний приклад
- Запускай, експериментуй, змінюй — патерни запам'ятовуються на практиці
- Додавай свої варіанти реалізації

---

## 🤝 Контрибуції

Буду рада ідеям, прикладам та покращенням! Форкни, покращуй — і присилай p
