# Weekly Task 3
# Veronica Curry
# Write a program that asks the user to input a string
# Output will revert every second letter

## References:
# https://www.youtube.com/watch?v=ajrtAuDg3yw
# https://www.w3schools.com/python/python_howto_reverse_string.asp
# 

# sentence to enter - The quick brown fox jumps over the lazy dog.


# need to figure out how to reverse a phrase [::-1]
# delete every second letter or choose only every second letter [::-2]
# how to choose everysecond letter  // Slicing 


# ask for a phrase
phrase = input ( "Please submit a phrase: ")
print ( "Your phrase is: " + phrase +"\nWe will now return this reverted")

# phrase reverted
print ( "Your phrase reverted is: " + (phrase[::-1]))

# phrase revert minus every second letter
print ( "Your phrase revert and missing every second letter is: " + (phrase[::-2]))
