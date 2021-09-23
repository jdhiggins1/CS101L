########################################################################
##
## CS 101 Lab
## Assignment 3
## Jordan Higgins
## jdhkq5@umsystem.edu
##
## PROBLEM : Find their number based on remainders of 3, 5 ,7.
##
## ALGORITHM : 
##      1. Look for x in a range of 0-100, x = %3,5,7.
## 
## ERROR HANDLING:
##     
##
## OTHER COMMENTS:
##    
########################################################################
print('Welcome to the Flarsheim Guesser!')


play = True
while play == True:
    print('Please think of a number between and including 1 and 100.')

    remainder_3 = int(input('What is the remainder when your number is divided by 3 ?'))

    def remain_func(remainder_3):
        while remainder_3 < 0:
            print('The value entered must be 0 or greater')
            remainder_3 = int(input('What is the remainder when your number is divided by 3 ?'))
        while remainder_3 >= 3:
            print('The value entered must be less than 3')
            remainder_3 = int(input('What is the remainder when your number is divided by 3 ?'))


    remain_func(remainder_3)

    remainder_5 = int(input('What is the remainder when your number is divided by 5 ?'))
    remainder_7 = int(input('What is the remainder when your number is divided by 7 ?'))


    for x in range(0,101):
        if x %3 == remainder_3 and x %5 == remainder_5 and x %7 == remainder_7:
            their_number = x
    print('Your number was',their_number)
    print('How amazing was that\n')


    while True:
        again = str(input('Do you want to play again? Y to continue, N to quit ==> '))
        if again == 'Y' or again == 'y':
            break
        if again == 'n' or again == 'N':
            play = False
            break
    
    


