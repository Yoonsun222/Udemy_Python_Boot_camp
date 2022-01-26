direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text_amount ,shift_amount, direction_amount):
    answer_text = ''
    if direction_amount == 'decode':
        shift_amount *= -1
    for i in text_amount:
        if ord(i)+shift_amount >= ord('a') and ord(i)+shift_amount <= ord('z'):
            answer_text += chr((ord(i)+shift_amount))
        else:
            answer_text += chr((ord(i)-ord('a')+shift_amount)%26+ord('a'))

    return print(f"The {direction_amount} text is {answer_text}")

caesar(text ,shift, direction)