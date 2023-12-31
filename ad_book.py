from collections import UserDict

class Field:
    def __init__(self, value: str) -> None:
        self.value = value
    

class Name(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)


class Record:
    
    def __init__(self, name: Name, phone: Phone=None) -> None:
        self.name = name
        self.phones = [phone] if phone else []
        
    
    def add_phone(self, phone) -> None:
        if phone not in self.phones:
            self.phones.append(phone)

    def delete_phone(self, phone) -> None:
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone
    

class AddressBook(UserDict):
    
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
    
    def find_record(self, value: str) -> Record:
        return self.data.get(value)    


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')