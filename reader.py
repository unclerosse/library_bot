from string import ascii_letters


class Reader:
    RUS: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    RUS_UPPER: str = RUS.upper()
    
    def __init__(self, name: str, card_number: int, date_of_birth: str) -> None:
        self.check_name(name)
        self.check_card_number(card_number)
        self.check_date(date_of_birth)

        self._name = name
        self._card_number = card_number
        self._date_of_birth = date_of_birth 
    
    @classmethod
    def check_name(cls, name: str) -> None:
        if type(name) != str:
            raise TypeError('ФИО должны быть записаны ввиде строки')
        if len(name.split()) != 3:
            raise ValueError('ФИО записаны некорректно')
        
        letters: str = ascii_letters + cls.RUS + cls.RUS_UPPER
        for el in name.split():
            if len(el) < 3:
                raise ValueError('каждая часть ФИО должна быть длиннее двух символов')
            if len(el.strip(letters)) != 0:
                raise ValueError('ФИО должно включать в себя только буквенные символы и тире')

    @property
    def name(self) -> str:
        return self._name 
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.check_name(new_name)
        self._name = new_name

    @classmethod
    def check_card_number(cls, num: int) -> None:
        if type(num) != int:
            return TypeError('Номер читательского билета должен быть числом')
        if len(str(num)) != 8:
            return ValueError('Номер читательского билета должен состоять из 8 цифр')
    
    @property
    def card_number(self) -> str:
        return self._card_number
    
    @card_number.setter
    def card_number(self, num: int) -> None:
        self.check_card_number(num)
        self._card_number = num

    @classmethod
    def check_date(cls, date: str) -> None:
        if type(date) != str:
            raise TypeError('Дата должна быть строкой')
        if date[2] != '.' or date[5] != '.' or date[6:8] != '19' or date[6:8] != '20' or len(date) != 10:
            raise ValueError('Неверный формат даты')
        if date[6:8] == '20' and date[9] not in ['0','1']:
            raise ValueError('Неверный формат даты')

    @property
    def date_of_birth(self) -> str:
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date):
        self.check_date(date)
        self._date_of_birth = date