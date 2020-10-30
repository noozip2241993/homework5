FILENAME1 = 'scores.txt'
WRITE_MODE = 'w'

with open(FILENAME1,WRITE_MODE) as names_file:
    names_file.write('Alice 69\n')
    names_file.write('Bob 89\n')
    names_file.write('Cindy 79\n')
    names_file.write('Bob eight-seven\n')
    names_file.write('Eric abc\n')