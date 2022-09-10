class LetterBox:
    def __init__(self, letter=None, flag=True):
        self._flag = flag
        self._letter = letter

    def put_flag_up(self, new_letter):
        self._letter = new_letter
        self._flag = True

    def put_flag_down(self):
        self._flag = False
