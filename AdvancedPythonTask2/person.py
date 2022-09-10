from letters import Letter
from letter_box import LetterBox


class Person:
    def __init__(self, letter_content, received_letter_content=None, letter=None):
        self._letter = letter
        self._letter_content = letter_content
        self._received_letter_content = received_letter_content



    def write_letter(self):
        self._letter = Letter(self._letter_content)
        self._letter.mark_unread()

    def deliver_letter(self):
        return self._letter

    def receive_letter(self, letter_box):
        self._letter = letter_box._letter
        letter_box.put_flag_down()

    def read_letter(self):
        self._received_letter_content = self._letter._letter_contents
        self._letter.mark_as_read()
