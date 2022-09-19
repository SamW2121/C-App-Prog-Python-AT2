from person import Person
from letter_box import LetterBox

def play():
    """ Check that the letter in the letterBox says hello Alice
        >>> new_letter_box = LetterBox()
        >>> bob = Person("Hello Alice", None)
        >>> alice = Person("Hello Bob", None)
        >>> bob.write_letter()
        >>> new_letter_box.put_flag_up(bob.deliver_letter())
        >>> print(new_letter_box._letter._letter_contents)
        Hello Alice
        >>> alice.receive_letter(new_letter_box)
        >>> print(new_letter_box._flag)
        False
        >>> alice.read_letter()
        >>> print(new_letter_box._letter._read)
        True
        >>> alice.write_letter()
        >>> new_letter_box.put_flag_up(alice.deliver_letter())
        >>> print(new_letter_box._flag)
        True
        >>> bob.receive_letter(new_letter_box)
        >>> bob.read_letter()
        >>> print(new_letter_box._letter._letter_contents)
        Hello Bob
        """

    new_letter_box = LetterBox()
    bob = Person("Hello Alice", None)
    alice = Person("Hello Bob", None)
    bob.write_letter()
    new_letter_box.put_flag_up(bob.deliver_letter())


    alice.receive_letter(new_letter_box)
    alice.read_letter()
    alice.write_letter()
    new_letter_box.put_flag_up(alice.deliver_letter())
    bob.receive_letter(new_letter_box)
    bob.read_letter()

def main(test=False):
    if test:
        import doctest
        return doctest.testmod()
    play()

if __name__ == '__main__':
    print(main(test=True))


"""
    
encrypted_letter_content = "hello bob"
shift = 3
li = []
print("letter content: " + encrypted_letter_content)
#li is empty list for word to be converted into
for count, value in enumerate(encrypted_letter_content):
    value = ord(value) + shift
    li.append(chr(value))


decrypted_letter_content = ''.join(li)
li.clear()
print("encrypted content: " + decrypted_letter_content)
for count, value in enumerate(decrypted_letter_content):
    value = ord(value) - shift
    li.append(chr(value))

decrypted_letter_content = ''.join(li)
print("decrypted content: " + decrypted_letter_content)

"""
