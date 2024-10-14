from collections import UserDict

class Field:
    """Базовий клас для полів, таких як Name та Phone."""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Клас для зберігання імені контакту, успадковує Field."""
    pass


class Phone(Field):
    """Клас для зберігання і валідації номера телефону, успадковує Field."""
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError
        super().__init__(value)

    @staticmethod
    def is_valid_phone(phone):
        return phone.isdigit() and len(phone) == 10


class Record:
    """Клас для зберігання імені контакту та списку телефонів."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """Додає телефон до запису."""
        self.phones.append(Phone(phone))
        return self

    def remove_phone(self, phone):
        """Видаляє телефон з запису."""
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return self
        return None

    def edit_phone(self, old_phone, new_phone):
        """Редагує телефон у записі. ValueError, якщо старий номер не знайдено."""
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return self
        raise ValueError

    def find_phone(self, phone):
        """Знаходить телефон у записі."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        """Кастомне строкове представлення запису."""
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Ім'я контакту: {self.name.value}, телефони: {phones_str}"


class AddressBook(UserDict):
    """Клас для зберігання та управління записами контактів."""
    def add_record(self, record):
        """Додає запис до адресної книги."""
        self.data[record.name.value] = record
        return record

    def find(self, name):
        """Знаходить запис за іменем."""
        return self.data.get(name, None)

    def delete(self, name):
        """Видаляє запис за іменем."""
        if name in self.data:
            record = self.data[name]
            del self.data[name]
            return record
        raise ValueError

    def __str__(self):
        """Кастомне строкове представлення адресної книги."""
        result = ""
        for record in self.data.values():
            result += str(record) + "\n"
        return result.strip()
