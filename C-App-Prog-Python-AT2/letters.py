class Letter:
    def __init__(self, letter_contents=None, addressee=None, read=None):
        self._read = read
        self._letter_contents = letter_contents
        self._addressee = addressee

    def mark_as_read(self):
        self._read = True

    def mark_unread(self):
        self._read = False
