FILENAME3 = 'book.txt'
READ_MODE = 'r'
try:
    with open(FILENAME3) as names_file3:
        pass
except IOError as error:
    print(f'Unable to open file {FILENAME3}. Error message: {error}')
print('After the handling code, program keeps running')
wordlist = []
with open(FILENAME3,READ_MODE) as names_file3:
    for character in names_file3:
        wordlist += character
wordlist = [letter.upper() for letter in wordlist]
alpha = list(map(chr,range(65,91)))
for i in alpha:
    print(f'{i} {wordlist.count(i)}')
if wordlist.count(i) ==0:
    print('It does not have all letters.')
else:
    print('It has all letters')
