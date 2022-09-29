from letter_box import LetterBox
from postoffice import PostOffice
from alice import Alice
from bob import Bob
from charlie import Charlie


def play():
    """
    >>> alice = Alice("Hello Bob")
    >>> bob = Bob("Hello Alice")
    >>> charlie = Charlie()
    >>> alices_letter_box = LetterBox("Alice")
    >>> bobs_letter_box = LetterBox("Bob")
    >>> post_office = PostOffice()

    >>> alice.write_letter()
    >>> print(alice._letter._read)
    False
    >>> print(alice._encrypted_content)
    ['K', 'h', 'o', 'o', 'r', '#', 'E', 'r', 'e']
    >>> alice.deliver_letter(True, post_office)
    >>> print(post_office._letter._letter_contents)
    ['K', 'h', 'o', 'o', 'r', '#', 'E', 'r', 'e']
    >>> charlie.receive_letter(None, post_office, True)
    >>> print(charlie._letter._letter_contents)
    ['K', 'h', 'o', 'o', 'r', '#', 'E', 'r', 'e']
    >>> charlie.read_addressee()
    >>> print(charlie._addressee)
    Bob
    >>> charlie.deliver_letter(False, post_office, bobs_letter_box)
    >>> print(bobs_letter_box._flag)
    True
    >>> print(bobs_letter_box._letter._letter_contents)
    ['K', 'h', 'o', 'o', 'r', '#', 'E', 'r', 'e']
    >>> bob.receive_letter(bobs_letter_box)
    >>> print(bobs_letter_box._flag)
    False
    >>> print(bob._letter._letter_contents)
    ['K', 'h', 'o', 'o', 'r', '#', 'E', 'r', 'e']
    >>> bob.read_letter()
    >>> print(bob._letter._read)
    True
    >>> print(bob._decrypted_content)
    Hello Bob
    >>> bob.write_letter()
    >>> print(bob._letter._read)
    False
    >>> print(bob._encrypted_content)
    ['K', 'h', 'o', 'o', 'r', '#', 'D', 'o', 'l', 'f', 'h']
    >>> bob.deliver_letter(True, post_office)
    >>> print(post_office._letter._letter_contents)
    ['K', 'h', 'o', 'o', 'r', '#', 'D', 'o', 'l', 'f', 'h']
    >>> charlie.receive_letter(None, post_office, True)
    >>> print(post_office._letter._letter_contents)
    ['K', 'h', 'o', 'o', 'r', '#', 'D', 'o', 'l', 'f', 'h']
    >>> charlie.read_addressee()
    >>> charlie.deliver_letter(False, post_office, alices_letter_box)
    >>> print(alices_letter_box._flag)
    True
    >>> print(alices_letter_box._letter._letter_contents)
    ['K', 'h', 'o', 'o', 'r', '#', 'D', 'o', 'l', 'f', 'h']
    >>> alice.receive_letter(alices_letter_box)
    >>> print(alices_letter_box._flag)
    False
    >>> print(alice._letter._letter_contents)
    ['K', 'h', 'o', 'o', 'r', '#', 'D', 'o', 'l', 'f', 'h']
    >>> alice.read_letter()
    >>> print(alice._letter._read)
    True
    >>> print(alice._decrypted_content)
    Hello Alice
    """

    alice = Alice("Hello Bob")
    bob = Bob("Hello Alice")
    charlie = Charlie()
    alices_letter_box = LetterBox("Alice")
    bobs_letter_box = LetterBox("Bob")
    post_office = PostOffice()

    alice.write_letter()
    print(f"new letters read status: {alice._letter._read}")
    print(f"Alice encrypted letter: {alice._encrypted_content}")
    alice.deliver_letter(True, post_office)
    print(f"post office letter reads: {post_office._letter._letter_contents}")
    charlie.receive_letter(None, post_office, True)
    print(f"letter charlie holds reads: {charlie._letter._letter_contents}")
    charlie.read_addressee()
    print(f"this letter is going to: {charlie._addressee}")
    charlie.deliver_letter(False, post_office, bobs_letter_box)
    print(f"Bobs letter box is up: {bobs_letter_box._flag}")
    print(f"Bobs letter boxes letter reads:{bobs_letter_box._letter._letter_contents}")
    bob.receive_letter(bobs_letter_box)
    print(f"bobs letter box flag status: {bobs_letter_box._flag}")
    print(f"Bobs letter reads: {bob._letter._letter_contents}")
    bob.read_letter()
    print(f"letter read status: {bob._letter._read}")
    print(f"translated that means: {bob._decrypted_content}")
    bob.write_letter()
    print(f"new letters read status: {bob._letter._read}")
    print(f"Bobs encrypted letter: {bob._encrypted_content}")
    bob.deliver_letter(True, post_office)
    print(f"post office letter reads: {post_office._letter._letter_contents}")
    charlie.receive_letter(None, post_office, True)
    print(f"letter charlie holds reads: {post_office._letter._letter_contents}")
    charlie.read_addressee()
    charlie.deliver_letter(False, post_office, alices_letter_box)
    print(f"Alice letter box flag status: {alices_letter_box._flag}")
    print(f"Alices letter boxes letter reads: {alices_letter_box._letter._letter_contents}")
    alice.receive_letter(alices_letter_box)
    print(f"Alice letter box flag status: {alices_letter_box._flag}")
    print(f"Alices letter reads: {alice._letter._letter_contents}")
    alice.read_letter()
    print(f"letter read status: {alice._letter._read}")
    print(f"translated that means: {alice._decrypted_content}")



def main(test=False):
    if test:
        import doctest
        return doctest.testmod()
    play()


if __name__ == '__main__':
    print(main(test=True))





