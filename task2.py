FILENAME3 = 'book.txt'
READ_MODE = 'r'
FILENAME4 = "summary.txt"
WRITE_MODE = 'w'
try:
    with open(FILENAME3) as names_file3:
        pass
except IOError as error:
    print(f'Unable to open file {FILENAME3}. Error message: {error}')
print('After the handling code, program keeps running')
wordlist = []
names_file3 = open(FILENAME3,READ_MODE)
names_file4 = open(FILENAME4,WRITE_MODE)
with names_file3, names_file4:
    for character in names_file3:
        wordlist += character
    wordlist = [letter.upper() for letter in wordlist]
    alpha = list(map(chr,range(65,91)))
    for i in alpha:
        print(f'{i} {wordlist.count(i)}')
        names_file4.write(f'{i} {wordlist.count(i)}\n')
    if wordlist.count(i) ==0:
        names_file4.write('It does not have all letters.')
        print('It does not have all letters.')
    
    else:
        names_file4.write('It has all letters.')
        print('It has all letters')
    
