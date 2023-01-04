class Reader:
    def __init__(self, name: str, card_number: str) -> None:
        self.check_name(name)
        self.check_card_number(card_number)

        self._name = name
        self._card_number = card_number

    @property
    def name(self) -> str:
        return self._name 
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.check_name(new_name)
        self._name = new_name

    @classmethod
    def check_card_number(cls, num: str) -> None:
        if type(num) != str:
            return TypeError('Номер читательского билета должен быть строкой')
        if len(str(num)) != 8:
            return ValueError('Номер читательского билета должен состоять из 8 цифр')
    
    @property
    def card_number(self) -> str:
        return self._card_number
    
    @card_number.setter
    def card_number(self, num: str) -> None:
        self.check_card_number(num)
        self._card_number = num
