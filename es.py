# Read in a TXT File and output the numbers of e's it contains

# Week 7
# Task 7

# Veronica Curry
# Student ID: G00074924


# The program should take the file name from an argument on the command line
# read out a number - the total count of E's
# Capital / Not Capital isnt specified

import sys                          # 1. Import System 

with open (sys.argv[1]) as f:       # 2. Open the file as inputed through the command line 
    data = f.read()                 # 3. Set data as the file contents
    freq = data.count("e")          # 4. Set Frequency as the count of "e" in the file
    print (freq)                    # 5. Print Frequency


# Reference 1. https://www.gutenberg.org/files/1400/1400-0.txt
# Reference 2. https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python
# Reference 3. https://pythonexamples.org/python-count-number-of-characters-in-text-file/
# Reference 4. https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# Reference 5. https://realpython.com/python-command-line-arguments/
# Reference 6. https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# Reference 7. https://docs.python.org/3/library/sys.html




