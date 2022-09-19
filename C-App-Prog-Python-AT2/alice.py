from letters import Letter
from person import Person


class Alice(Person):
    def __init__(self):
        super().__init__()
        self._letter_content = ""
        self._recieved_letter_content = ""

    def write_letter(self):
        self._letter = Letter(self._letter_content, "Bob")
        self.encrypt_letter(self._letter)
        self._letter.mark_unread()

    def read_letter(self):
        self._received_letter_content = self._letter._letter_contents
        self._letter.mark_as_read()

    def encrypt_letter(self, letter=None):
        pass

    def decrypt_letter(self):
        pass
