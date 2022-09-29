from letters import Letter
from letter_box import LetterBox
from postoffice import PostOffice


class Person:
    def __init__(self,  addressee=None, letter=None):
        self._letter = letter
        self._addressee = addressee

    def deliver_letter(self, location=False, post_office=None, letter_box=None):
        # Will take letter written and assign it to instantiated post office object
        if location:
            post_office._letter = self._letter
        # Will check which address to take letter too and assign the letter boxes letter as the
        # letter being carried by person
        elif self._addressee == letter_box._address:
            letter_box.put_flag_up(self._letter)

    def receive_letter(self, letter_box=None, post_office=None, is_charlie=False):
        # is_charlie is only turned true when charlie is getting a letter from the post office
        if is_charlie:
            self._letter = post_office._letter
        if not is_charlie:
            self._letter = letter_box._letter
            letter_box.put_flag_down()
