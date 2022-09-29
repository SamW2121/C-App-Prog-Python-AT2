from person import Person


class Charlie(Person):

    def __init__(self, ):
        super().__init__()

    def read_addressee(self):
        self._addressee = self._letter._addressee
