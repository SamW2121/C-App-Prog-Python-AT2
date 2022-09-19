from person import Person


class Bob(Person):
    def __init__(self):
        super().__init__()
        self._letter_content = ""
        self._recieved_letter_content = ""

    def write_letter(self):
        pass

    def read_letter(self):
        pass

    def encrypt_letter(self):
        pass

    def decrypt_letter(self):
        pass
