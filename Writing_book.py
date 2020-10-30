FILENAME3 = 'book.txt'
WRITE_MODE = 'w'
with open(FILENAME3,WRITE_MODE) as names_file3:
    names_file3.write("Read a text file named “book.txt” that may have multiple lines. Then create a “summary.txt”\nfile that has the frequency of each letter, case-insensitive, i.e., “a” and “A” are the same letter.\nEach line has a record of the letter and frequency.The last line should be a summary to tell if\nthe file has all 26 letters." )
