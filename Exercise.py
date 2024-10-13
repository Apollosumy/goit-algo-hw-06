from collections import UserDict

class Field:
    """Базовий клас для полів, таких як Name та Phone."""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Клас для зберігання імені контакту, наслідується від Field."""
    pass


class Phone(Field):
    """Клас для зберігання і валідації номера телефону, наслідується від Field."""
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Невірний формат номера телефону. Повинно бути 10 цифр.")
        super().__init__(value)

    @staticmethod
    def is_valid_phone(phone):
        return phone.isdigit() and len(phone) == 10


class Record:
    """Клас для зберігання імені контакту та списку телефонних номерів."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """Додає телефон до запису."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """Видаляє телефон із запису."""
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return f"Телефон {phone} видалено."
        return "Телефон не знайдено."

    def edit_phone(self, old_phone, new_phone):
        """Редагує телефон у записі."""
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return f"Телефон {old_phone} оновлено на {new_phone}."
        return "Старий номер телефону не знайдено."

    def find_phone(self, phone):
        """Шукає телефон у записі."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        """Користувацьке рядкове представлення запису."""
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Ім'я контакту: {self.name.value}, телефони: {phones_str}"


class AddressBook(UserDict):
    """Клас для зберігання та управління контактними записами."""
    def add_record(self, record):
        """Додає запис до адресної книги."""
        self.data[record.name.value] = record

    def find(self, name):
        """Знаходить запис за іменем."""
        return self.data.get(name, None)

    def delete(self, name):
        """Видаляє запис за іменем."""
        if name in self.data:
            del self.data[name]
            return f"Запис для {name} видалено."
        return "Запис не знайдено."

    def __str__(self):
        """Користувацьке рядкове представлення адресної книги."""
        result = ""
        for record in self.data.values():
            result += str(record) + "\n"
        return result.strip()


