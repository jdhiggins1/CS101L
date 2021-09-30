########################################################################
##
## CS 101 Lab
## Program # 5
## Jordan Higgins
## JDHKQ5@Umsystem.edu
##
## PROBLEM : Use functions to create a slot machine.
##
## ALGORITHM : 
##      1. 
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random



match = 0
def play_again() -> bool:
    again = str(input('Do you want to play again? Y/N'))
    if again == 'n' or again == 'N': 
        return False
    if again == 'Y' or again == 'y':
        return True
    else: print('You must enter Y/YES/N/NO to continue. Please try again'), play_again()
    return True
     
def get_wager(bank : int) -> int:
    global bet_amount
    bet_amount = int(input('How many chips would you like to wager?'))
    if bet_amount > start_wage:
        print('The wager amount cannot be greater than how much you have.')
        get_wager(bank)
    elif bet_amount <= 0:
        print('The wager amount must be greater than 0.Please enter again.')
    else: return bet_amount
  
def get_slot_results() -> tuple:
    reela = random.randint(0,10)
    reelb = random.randint(0,10)
    reelc = random.randint(0,10)

    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    if reela == reelc and reela == reelb:
        print('All 3 match')
        match = 3
    elif reela == reelb or reela == reelc or reelc == reelb:
        match = 1
    else: match = 0
    return match

def get_bank() -> int:
    while True:
        global start_wage
        start_wage = int(input('How many chips do you want to start with?'))
        if start_wage > 0 and start_wage < 101:
            return start_wage
            break
        else: print('Try again')

    return start_wage

def get_payout(wager, matches):
    if match == 3:
        payout = bet_amount * 10
    elif match ==1:
        payout = (bet_amount * 3) - get_wager
    else: payout = bet_amount * -1 
        
    return payout     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()