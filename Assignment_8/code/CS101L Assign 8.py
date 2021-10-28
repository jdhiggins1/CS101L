import math

tests_scores = []
prgms_lst = []
def display_scores():
    prgm_count = len(prgms_lst)
    test_count = len(tests_scores)
    result = list(map(int, tests_scores))
    prgm_result = list(map(int, prgms_lst))
    print('Type               #       min       max       avg       std')
    print('============================================================')
    if not tests_scores and not prgms_lst:
        print('Tests              0       n/a       n/a       n/a       n/a')
        print('Programs           0       n/a       n/a       n/a       n/a\n')
        print('The weighted scores is       0.00')
    if not tests_scores and len(prgms_lst) > 0:
        print('Tests              0       n/a       n/a       n/a       n/a')
    if len(result) > 0:
        tsubtracted_mean = []
        for i in range(len(result)):
            test_mean = sum(result)/test_count
            tsubtracted_mean.append(result[i] - test_mean)
        tsubtracted_mean = [number ** 2 for number in tsubtracted_mean]
        tsubtracted_mean = list(map(int, tsubtracted_mean))
        tsubtracted_mean = sum(tsubtracted_mean)/test_count
        std = math.sqrt(tsubtracted_mean)
        std = "{:.2f}".format(std)
        test_mean = "{:.2f}".format(test_mean)
        print('Tests              {}       {}       {}       {}       {}'.format(test_count,min(tests_scores),max(tests_scores),test_mean,std))
    if len(prgm_result) > 0:
        prgm_form = []
        for i in range(len(prgm_result)):
            prgm_mean = sum(prgm_result)/prgm_count
            prgm_form.append(prgm_result[i] - prgm_mean)
        prgm_form = [number ** 2 for number in prgm_form]
        prgm_form = list(map(int, prgm_form))
        prgm_form = sum(prgm_form)/prgm_count
        std = math.sqrt(prgm_form)
        std = "{:.2f}".format(std)
        weight_score = (float(test_mean) * .6) + (prgm_mean * .4)   
        weight_score = (float(test_mean) * .6) + (prgm_mean * .4)  
        prgm_mean = "{:.2f}".format(prgm_mean) 
        weight_score = "{:.2f}".format(weight_score)
        print('Programs           {}       {}       {}       {}       {}\n'.format(prgm_count,min(prgms_lst),max(prgms_lst),prgm_mean,std))
        if not prgms_lst and len(tests_scores) > 0:
            print('Programs           0       n/a       n/a       n/a       n/a\n')
            print('The weighted scores is       0.00')
        print('The weighted scores is       ',weight_score)

def test_add():
    again = True
    while again == True:
        add_test = input('Enter the new Test score 0-100 ')
        if int(add_test) < 0:
            print('Score cannot be less than 0')
        else:
            tests_scores.append(add_test)
            again = False

def test_remove():
    while True:
        user_remove = input('Enter the score of the test you want to remove ')
        try:
            tests_scores.remove(user_remove)
        except ValueError:
            print('Score does not exist')
            continue
        break

def clear_tests():
    tests_scores.clear()
    print('List succesfully cleared')

def prgm_add():
    again = 0
    while again == 0:
        add_prgm = input('Enter the new Assignment score 0-100 ')
        if int(add_prgm) < 0:
            print('Score cannot be less than 0')
        prgms_lst.append(add_prgm)
        again = 1


def prgm_remove():
    while True:
        user_remove = input('Enter the score of the program you want to remove ')
        try:
            prgms_lst.remove(user_remove)
        except ValueError:
            print('Score does not exist')
            continue
        break

def prgm_clear():
    prgms_lst.clear()
    print('List successfully cleared')

def main():
    play = True
    print('\t Grade Menu')
    user_selection = input('1 -Add Test\n2 -Remove Test\n3 -Clear Tests\n4 -Add Assignment\n5 -Remove Assignment\n6 -Clear Assignments\nD -Display Scores\nQ -Quit\n\n==> ')
    while play == True:
        if user_selection == 'd' or user_selection == 'D':
            display_scores()
        elif user_selection == '1':
            test_add()
        elif user_selection == '2':
            test_remove()
        elif user_selection == '3':
            clear_tests()
        elif user_selection == '4':
            prgm_add()
        elif user_selection == '5':
            prgm_remove()
        elif user_selection == '6':
            prgm_clear()
        elif user_selection == 'q' or user_selection == 'Q':
            play = False
        else: print('You must enter a valid option. (1,2,3,4,5,6,D,Q)')
        user_selection = input('1 -Add Test\n2 -Remove Test\n3 -Clear Tests\n4 -Add Assignment\n5 -Remove Assignment\n6 -Clear Assignments\nD -Display Scores\nQ -Quit\n\n==> ')
main()
