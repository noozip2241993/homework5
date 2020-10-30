import os
FILENAME1 = 'scores.txt'
READ_MODE = 'r'
FILENAME2 = 'log.txt'
WRITE_MODE = 'w'
try:
    with open(FILENAME1) as names_file1:
        pass
except IOError as error:
    print(f'Unable to open file {FILENAME1}. Error message: {error}')
print('After the handling code, program keeps running')



total_student = 0
total_score = 0
names_file1 = open(FILENAME1,READ_MODE)
names_file2 = open(FILENAME2,WRITE_MODE)
with names_file1, names_file2:
    for line in names_file1:
        info= line.split()
        try:
            if int(info[1]) >= 0 and int(info[1]) < 100:
                total_student = total_student + 1
                total_score = total_score + int(info[1])
        except ValueError as error:
            names_file2.write(f'Bad score value for {info[0]}, ignored.\n')
    names_file2.write(f'The class average is {total_score/total_student:.0f} for {total_student} students.')
    print(f'The class average is {total_score/total_student:.0f} for {total_student} students.')