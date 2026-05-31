str_original = input()

new_string = ""

for caractere in str_original:

    if caractere == '0':
        new_string = new_string + '1'

    else:
        new_string = new_string + caractere
print(new_string)