from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self,value:str):
        if len(value) < 1 or value.strip() == '':
            raise ValueError ('Enter correct Name')
        super().__init__(value)

class Phone(Field):
    def __init__(self,value:str):
         if not value.isdigit() or len(value) != 10:
            raise ValueError ('The phone number must  consist of exactly 10 digits')
         super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone:str):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)
        return phone_obj

    def remove_phone(self,phone:str):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    def edit_phone(self, old_phone: str, new_phone: str):
        new_obj = Phone(new_phone)  # валидация нового номера
        for item in self.phones:
            if item.value == old_phone:
                item.value = new_obj.value
                return
        raise ValueError(f"{old_phone} doesn't exist")

    def find_phone(self,phone:str)->Phone | None:
        for item in self.phones:
            if item.value == phone:
                return item
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def __str__(self):
        if not self.data:
            return "AddressBook is empty"
        return "\n".join(str(record) for record in self.data.values())

    def add_record(self,record:Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact '{name}' not found")




