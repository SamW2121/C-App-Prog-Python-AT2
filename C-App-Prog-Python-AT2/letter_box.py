class LetterBox:
    def __init__(self,  address=None, letter=None, flag=False):
        self._flag = flag
        self._letter = letter
        self._address = address

    def put_flag_up(self, new_letter):
        self._letter = new_letter
        self._flag = True

    def put_flag_down(self):
        self._flag = False
