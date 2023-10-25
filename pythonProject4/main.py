def encode(passw):
    new_pass = ''
    for i in passw:
        if 0 <= int(i) <= 6:
            new_pass += str(int(i) + 3)
        elif int(i) == 7:
            new_pass += '0'
        elif int(i) == 8:
            new_pass += '1'
        elif int(i) == 9:
            new_pass += '2'
    return new_pass

def decode(passw):
    dec_pass = ''
    for i in passw:
        if 3 <= int(i) <= 9:
            dec_pass += str(int(i) - 3)
        elif int(i) == 2:
            dec_pass += '9'
        elif int(i) == 1:
            dec_pass += '8'
        elif int(i) == 0:
            dec_pass += '7'
    return dec_pass



encoded_pass = ''
decoded_pass = ''


# Press the green button in the gutter to run the script.
while __name__ == '__main__':
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    option = int(input('Please enter an option: '))



    if option == 1:
        input_pass = input('Please enter your password to encode: ')
        encoded_pass = encode(input_pass)
        print('Your password has been encoded and stored!')

    elif option == 2:
        decoded_pass = decode(encoded_pass)
        print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}.')
    elif option == 3:
        exit()

