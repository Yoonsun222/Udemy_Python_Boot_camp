alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_amount ,shift_amount):
    ciher_text = ''

    for i in text_amount:
        if ord(i)+shift >= ord('a') and ord(i)+shift <= ord('z'):
            ciher_text += chr((ord(i)+shift_amount))
        else:
            ciher_text += chr((ord(i)-ord('a')+shift_amount)%26+ord('a'))
    
    return ciher_text


def decrypt(cipher_text, shift_amount):
    decoded_text = ''

    for i in cipher_text:
        if ord(i)-shift <= ord('z') and ord(i)-shift >= ord('a'):
            decoded_text += chr((ord(i)-shift_amount))
        else:
            decoded_text += chr((ord(i)-ord('a')+shift_amount)%26+ord('a'))
    
    return decoded_text

if direction == 'encode':
    print(f"The encoded text is {encrypt(text, shift)}")
elif direction == 'decode':
    print(f"The decoded text is {decrypt(text, shift)}")