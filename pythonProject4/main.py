# Cole Andre
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


# Alyssa's Decode below:
def decode(password):
    decoded_password = []
    for i in range(0, len(password)):
        # keeps numbers from being negative after subtracting 3
        if password[i] == '0':
            decoded_password.append('7')
        elif password[i] == '1':
            decoded_password.append('8')
        elif password[i] == '2':
            decoded_password.append('9')
        else:
            decoded_password.append(int(password[i]) - 3)
        # interation
        i += 1
    decoded_password_string = ''
    # converts list back into a string
    for i in range(0, len(decoded_password)):
        decoded_password_string += str(decoded_password[i])
        i += 1
    return decoded_password_string


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
