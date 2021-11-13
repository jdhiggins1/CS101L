import string

d = dict()
def get_file():
    while True:
        try:
            user_file = input('Enter the name of the file to open ')
            file = open(user_file, 'r')
            return file
        except FileNotFoundError:
            print('Could not open file', user_file)
        except IOError:
            print('IO Error', user_file)


        
def freq_words(file):
    lines = file.readlines()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    counter = 0
    for line in lines:
        words = line.split()
        for x in words:
            character = x[len(x)-1]
            if character in punctuations:
                counter = counter +1 
    
    for i in range(len(lines)):
            lines[i] = lines[i].lower()
    lines = [''.join(c for c in s if c not in string.punctuation) for s in lines]
    for x in lines:
        words = x.split()
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    print("{:<10} {:<10} {:<10}".format('#', 'Word', 'Freq.'))
    print('===========================')
    
    
    for key in list(d.keys()):
        occure_once = 0
        sorted(d, key=d.get, reverse=True)[:10]
        print("{:<10} {:<10} {:<10}".format(key,key, d[key]))
        if d[key] == 1:
            occure_once = occure_once + 1
    print('There are',occure_once,'words that occur only once')
    unique_words = int(len(d))/2
    print('There are',unique_words,'unique words in the document')
    print('There are',counter,'punctuation marks in the document')


def main(): 
    file = get_file()
    freq_words(file)

main()

