############################################################################
# ## CS 101 Lab
# ## Program #6
# ## Jordan Higgins
# ## JDHKQ5@umsystem.edu
# ## PROBLEM : Encode and decode a string base off ascii values and shifting by user input.
# ## ALGORITHM : 
#      1. Used function inorder to splice the string into a list, ord it into a value and shift it by user_shift.
# ## ERROR HANDLING: 
# ##      Any Special Error handling to be noted.  Wager not less than 0. etc
# ## OTHER COMMENTS:
#
# ##  Tricky part of this code was getting the spaces to not change ascii values, in order to do this, I simply set the list != [Space], did the shift to the ones that do not
# ##  equal space, append them to a list, then append the [Space] afterwards.
# ##########################################################################




import string
play = True

def encode_string():
    user_string = str(input('Enter a (brief) text to encrypt:'))
    user_shift = (int(input('Enter the number to shift letters by:')))
    string_list = []
    for char in user_string:
        ascii_char = ord(char)
        if ascii_char != 32:
            temp = ascii_char + user_shift
            temp = chr(temp)
            string_list.append(temp)
        else: 
            string_list.append(' ')
    string_list = ''.join(map(str, string_list))
    finished_encoded = string_list.upper()
    print('Encrypted:',finished_encoded,'\n')
    
def decode_string():
    user_string = str(input('Enter a (brief) text to encrypt:'))
    user_shift = (int(input('Enter the number to shift letters by:')))
    string_list = []
    for char in user_string:
        ascii_char = ord(char)
        if ascii_char != 32:
            temp = ascii_char - user_shift
            temp = chr(temp)
            string_list.append(temp)
        else: 
            string_list.append(' ')
    string_list = ''.join(map(str, string_list))
    finished_encoded = string_list.upper()
    print('Decrypted:',finished_encoded)
  


while play == True:
    print('MAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')
    user_selection = str(input('Enter your selection ==> '))


    if user_selection == '1':
        encode_string()

    elif user_selection =='2':
        decode_string()

    elif user_selection == 'Q':
        print('Have an ordinary day')
        play = False

    else: print('Entry not valid')



