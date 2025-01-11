# Лабораторная работа №7: Работа с классами ч.3

## Описание работы
В данной лабораторной работе рассматриваются продвинутые концепции объектно-ориентированного программирования (ООП) в Python, такие как множественное наследование, инкапсуляция и полиморфизм. Учащиеся разрабатывают систему управления сотрудниками, которая включает различные типы сотрудников: менеджеров, технических специалистов и технических менеджеров. Работа демонстрирует, как комбинировать функциональность нескольких классов с помощью множественного наследования и как использовать полиморфизм для работы с различными типами сотрудников.

## Задание

1. **Создание базового класса `Employee`**:
   - Класс содержит общие атрибуты, такие как `name` (имя) и `id` (идентификационный номер).
   - Метод `get_info()` возвращает базовую информацию о сотруднике.

2. **Создание класса `Manager`**:
   - Наследует от `Employee` и добавляет атрибут `department` (отдел).
   - Метод `manage()` символизирует управление проектами.

3. **Создание класса `Technician`**:
   - Наследует от `Employee` и добавляет атрибут `specialization` (специализация).
   - Метод `maintenance()` символизирует выполнение технического обслуживания.

4. **Создание класса `TechManager`**:
   - Наследует от `Manager` и `Technician`, комбинируя управленческие и технические навыки.
   - Добавляет методы для управления командой сотрудников.

5. **Демонстрация функциональности**:
   - Создаются объекты каждого класса, и демонстрируется их функциональность.

## Реализация

### Класс `Employee`
```python
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        pass

    def get_info(self):
        return f"{self.name=}, {self.id=}"
```

### Класс `Manager`
```python
class Manager(Employee):
    def __init__(self, name, id, department, *args):
        super().__init__(name, id, *args)
        self.department = department

    def get_info(self):
        return super().get_info() + f" {self.department=}"

    def manage(self):
        return f"Manager - {self.department}"
```

### Класс `Technician`
```python
class Technician(Employee):
    def __init__(self, name, id, specialization, *args):
        super().__init__(name, id, *args)
        self.specialization = specialization

    def get_info(self):
        return super().get_info() + f" {self.specialization=}"

    def maintenance(self):
        return f"Maintenance - {self.maintenance}"
```

### Класс `TechManager`
```python
class TechManager(Manager, Technician):
    def __init__(self, name, id, department=None, specialization=None, *args):
        super().__init__(name, id, department, specialization)
        self.team = []

    def add_employee(self, data):
        self.team.append(data)

    def get_team_info(self):
        return self.team
```

### Пример использования
```python
emp = TechManager("Azbek", 1, "IT", "Tester")

print(emp.get_info())

emp.add_employee(Employee("Jzamshut", 2))
emp.add_employee(Manager("Ashot😎", 3, "Uborshik🪣"))

for i in emp.get_team_info():
    print(i.get_info())
```

## Заключение
В ходе выполнения лабораторной работы были освоены продвинутые концепции ООП в Python, такие как множественное наследование, инкапсуляция и полиморфизм. Учащиеся научились создавать сложные иерархии классов и комбинировать функциональность нескольких классов для решения практических задач.