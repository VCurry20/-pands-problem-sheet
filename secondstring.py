# Write a program asks for input - string; outputs every second letter in reverse
# Week 3
# Task 3

# Veronica Curry
# Student ID: G00074924

# sentence to enter: The quick brown fox jumps over the lazy dog.

#Methodology:
# need to figure out how to reverse a phrase [::-1]
# delete every second letter or choose only every second letter [::-2]
# how to choose everysecond letter  // Slicing 
# include the full stop """


phrase = input ( "Please submit a phrase: ")                                            # 1.
print ( "Your phrase is: " + phrase +"\nWe will now return this reverted")              # 2.

print ( "Your phrase reverted is: " + (phrase[::-1]))                                   # 3.

print ( "Your phrase revert and missing every second letter is: " + (phrase[::-2]))     # 4.
 
# 1. Set variable from input "Please submit a phrase: "
# 2. Print " Your phrase ( returns variable) \ new line - "We will now return this reverted"

# 3. Print " Your phrase reverted is " (Variable Phrase - from beginning to the end reverted written to the power of minus one - Sliced minus 1)

# 4.Print " Your phrase reverted is and is missing evert second letter is " (Variable Phrase - from beginning to the end reverted written to the power of minus two - Sliced minus 2)




# Reference 1 - Python Tutorial - https://www.youtube.com/watch?v=ajrtAuDg3yw
# Reference 2 - W3 Schools - https://www.w3schools.com/python/python_howto_reverse_string.asp
# Reference 3 - Slicing Blog - https://www.saltycrane.com/blog/2009/04/how-reverse-words-sentence-using-python-and-c/
