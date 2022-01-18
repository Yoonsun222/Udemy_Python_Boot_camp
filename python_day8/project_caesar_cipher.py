from art import logo


print(logo)

state = True
while state == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(text_amount ,shift_amount, direction_amount):
        answer_text = ''
        if direction_amount == 'decode':
            shift_amount *= -1
        for i in text_amount:
            if i >= 'a' and i <= 'z':
                if ord(i)+shift_amount >= ord('a') and ord(i)+shift_amount <= ord('z'):
                    answer_text += chr((ord(i)+shift_amount))
                else:
                    answer_text += chr((ord(i)-ord('a')+shift_amount)%26+ord('a'))
            else:
                answer_text += i

        return print(f"The {direction_amount} text is {answer_text}")

    caesar(text ,shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if restart == 'no':
        state = False
