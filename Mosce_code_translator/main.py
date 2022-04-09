
morse_code_alphabet ={

                    'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', '+':'.-.-.',
                    '&':'.-...', '!':'-.-.--', '$':'...-..-', '@':'	.--.-.',
                    '=':'-...-', ' ': ' '
}


def encrypt_text_to_morse_code( ):
    """
    :param string_value: take a sequence of letter as sting
    :return:  the corresponding Morse code
    """
    string_value = input( 'Please enter your message here: ')
    cypher_text = ''
    code = string_value.upper()
    for i in range(0, len(string_value)-1):
        if string_value[i] == ' ':
            cypher_text += ' '
        else:
            cypher_text += morse_code_alphabet[code[i]] + ' '

    print(f" Your message is: {cypher_text}")


def morse_code_decoder():
    """
    take a Morse code text
    :return:  plain English text
    """
    message = input("please enter your message here: ").split( ' ')
    decrypt = {value: key for key, value in morse_code_alphabet.items()}

    de_cipher_text = ''

    for letter in message:
        if letter == ' ':
            de_cipher_text += ' '
        else:
            de_cipher_text += decrypt[letter]

    print(f" Your message is : {de_cipher_text}")


running = 1
while running == 1:

    try:
        job = int(input("What do you want to do today? please enter  1 for encode or  2 for decode: "))
        if  job == 1:
            encrypt_text_to_morse_code()
        else:
            morse_code_decoder()

    except KeyError as err:
        print('Please enter a message')
    finally:
        running = int(input('What else do you want to do?  enter 1 to continue or 0 to terminate the program: '))


