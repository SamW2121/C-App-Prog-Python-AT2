from letters import Letter
from person import Person


class Alice(Person):
    def __init__(self, letter_content=None, received_letter_content=None):
        super().__init__("Bob")
        self._letter_content = letter_content
        self._received_letter_content = received_letter_content
        self._encrypted_content = []
        self._decrypting_list = []
        self._decrypted_content = ""

    def write_letter(self):
        self.encrypt_letter(self._letter_content, self._encrypted_content)
        self._letter = Letter(self._encrypted_content, self._addressee)
        self._letter.mark_unread()

    def read_letter(self):
        self._encrypted_content = self._letter._letter_contents
        self.decrypt_letter(self._encrypted_content, self._decrypting_list)
        self._letter.mark_as_read()

    def encrypt_letter(self, letter_content=None, encrypted_list=None, shift=3):
        for value in letter_content:
            value = ord(value) + shift
            encrypted_list.append(chr(value))

    def decrypt_letter(self, encrypted_list=None, decrypted_list=None, shift=3):
        for value in encrypted_list:
            value = ord(value) - shift
            decrypted_list.append(chr(value))
        self._decrypted_content = ''.join(decrypted_list)
