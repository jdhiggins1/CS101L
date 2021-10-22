
def get_minmpg():
    global min_mpg
    min_mpg = 0
    while min_mpg == 0:
        min_mpg = input('Enter the minimum mpg ==> ')
        if min_mpg.isnumeric() == False:
            print('You must enter a number for the fuel economy')
            min_mpg=0
        elif int(min_mpg) <= 0:
            print('Fuel economy given must be greater than 0')
            min_mpg=0
        elif int(min_mpg) >= 100:
            print('Fuel economy must be less than 100')
            min_mpg=0
        else:
            return int(min_mpg)


def get_file():
    while True:
        try:
            file_name = str(input('Enter the name of the input vehicle file ==> '))
            file = open(file_name,'r')
            return file
        except FileNotFoundError:
            print('Could not open file',file_name)
        except IOError:
            print('There is an IO Error',file_name)


def find_by_mpg(file, min_mpg):
    lines = file.readlines()
    cars = []
    for line in lines:
       mpg = line.split('\t')[7]
       if mpg.isnumeric() and int(mpg) > min_mpg:
            year = line.split('\t')[0]
            make = line.split('\t')[1]
            model = line.split('\t')[2]
            cars.append((year, make, model, mpg))
    return cars


def output_to_file(cars):
    while True:
        try:
            file_name = str(input("Enter the name of the file to output to ==> "))
            file = open(file_name,'w')
            break
        except FileNotFoundError:
            print('Could not open file',file_name)
        except IOError:
            print('There is an IO Error',file_name)
    
    for car in cars:
        file.write("{:<40} {:<40} {:<40} {:>10} \n".format(car[0], car[1], car[2], car[3]))
    file.close()



def main():
    min_mpg = get_minmpg()
    file = get_file()
    cars = find_by_mpg(file, min_mpg)
    output_to_file(cars)
    file.close()

main()


