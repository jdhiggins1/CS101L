import string


def get_librarycard():
    global library_card
    library_card = str(input('Enter Library Card. Hit Enter to Exit ==> '))

def get_school():
    if library_card[5] == '1':
        print('School of engineering')
    elif library_card[5] == '2':
        print('School of law')
    elif library_card[5] == '3':
        print('College of Arts and Sciences')
    else: print('not a 1 2 or 3')

def get_grade():
    if library_card[6] == '1':
        print('Freshman')
    elif library_card[6] == '2':
        print('Sophomore')
    elif library_card[6] == '3':
        print('Junior')
    elif library_card[6] == '4':
        print('Senior')
    else: print('not a 1 2 3 or 4 get_grade()')

def character_value():
    ascii_values = [ord(i) for i in library_card]
    for x in ascii_values[:5]:
        print(int(x)-65)
    for x in ascii_values[5:]:
        print(int(x)-49)
    

def get_check_digit():
    for i in library_card:
        index = library_card.index(i)
        print(i)


def verify_check_digit():
    if len(library_card) != 10:
        print('The length of the number given must be 10')
    elif library_card[:5].isupper() == False:
        print('The first 5 characters msut be A-Z, the invalid character is a 3 is %')
    elif library_card[7:10].isdigit() == False:
        print('The last 3 characters must be 0-9, the invalid chracter is at 7 is X')
    elif int(library_card[5]) > 4 or int(library_card[5]) < 0:
        print(library_card[5])    
    elif int(library_card[6]) > 5 or int(library_card[6]) < 0:
        print('The seventh character must be 1 2 3 or 4')
    else: print('Passed all checks')

       

get_librarycard()
verify_check_digit()
get_school()
get_grade()
character_value()
get_check_digit()
