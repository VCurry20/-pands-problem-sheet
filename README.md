# -pands-problem-sheet

# Weekly Tasks for PANDS 2021 
Author Veronica Curry

Student ID: G00074924

This file contains the overview for the 7 weekly tasks for the Programing and Scripting Module, GMIT, 2021.


<br/>
<br/>


# Task 1  - BMI


> File - [BMI.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/BMI.py)

> Objective - Write a program that calculates a person's BMI

> Input - Person's height in centimetres and weight in kilograms

> Output - BMI - weight divided by height in metres SQ


## Code:

```ruby
name = input ('Enter your name: ')                                          
print('Hello ' + name + '\nNice to meet you, lets calculate your BMI!')     

height = float(input('Enter your height in CM: '))                          
heightinmeters = height / 100                                              
print('Your height in meters is {}'.format(heightinmeters))                 

weight = float(input("Input your weight in Kilogram: "))                    
print('Your weight is {}'.format(weight))                                   

BMI = (round(weight / (heightinmeters * heightinmeters), 2))                
print ( " Your BMI is {}".format (BMI)) 
```

This Program asks the user to input their name and greets them. The user is then asked to input their height in CM, which is converted to Metres. This is then confirmed to the user. The Users weight is then requested and confirmed. Height and Weight are saved as variables allowing multiple users to use the program inputting their own specific data. Height and Weight are formatted as floats as opposed to string input from questions. These variables are then passed through the formula. The last output the user sees is their BMI confirmed to them.

> BMI formula (weight / (height * height), 2)


References:

- Kings Weightloss Clinic, BMI Checker (No Date), http://www.kingsweightlossclinics.co.uk/resources/bmi-checker/ (Accessed: February 2021)
- Stack Overflow, BMI Calculator Python (2014), https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/50386292#:~:text=')%20while%20input%20%3D%3D%20'imperial,which%20means%20you%20are%20underweight. (Accessed: February 2021)
- Code Review, Simple BMI Calculator (2020) https://codereview.stackexchange.com/questions/217751/simple-bmi-calculator-python-3 (Accessed: February 2021)
- Slimming World, BMI Calculator (No Date) https://www.slimmingworld.ie/bmi-calculator (Accessed: February 2021)


<br/>

# Task 2  - Second String


> File - [secondstring.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/secondstring.py)

> Objective - Write a program that asks for a input and outputs every second letter in reverse

> Input - The quick brown fox jumps over the lazy dog.

> Output - .o zletrv pu o wr cu h


## Code:

```ruby
phrase = input ( "Please submit a phrase: ")                                            
print ( "Your phrase is: " + phrase +"\nWe will now return this reverted")              

print ( "Your phrase reverted is: " + (phrase[::-1]))                                  

print ( "Your phrase revert and missing every second letter is: " + (phrase[::-2]))
```

This code asks the user for an input - example " The quick brown fox jumps over the lazy dog." . The program reverts this input and returns the sentence missing every second letter - example output ".o zletrv pu o wr cu h". This program uses slicing and also reversing.


References:

- Youtube, Python Tutorial: Slicing lists and Strings (Oct 29, 2015) - https://www.youtube.com/watch?v=ajrtAuDg3yw (Accessed: February 2021)
- W3 Schools, How to reverse a string, (No Date) - https://www.w3schools.com/python/python_howto_reverse_string.asp (Accessed: February 2021)
- Salty Crane Blog, How to reverse words in a sentence using Python and C (April 22, 2009) - https://www.saltycrane.com/blog/2009/04/how-reverse-words-sentence-using-python-and-c/ (Accessed: February 2021)
- Educative.io, How do you reverse a string in Python? (No Date) - https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python (Accessed: February 2021)
<br/>

# Task 3  - Collatz


> File - [collatz.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/collatz.py)

> Objective - Write a program that asks users to input a positive integer and outputs a list of successive values - successive values calculated as follows - if even divide by two, if odd multiply by three and add one. Program stops at zero.

> Input - 10

> Output - 10,5,16,8,4,2,1


## Code:

```ruby
def formula (number):                                           
    if (number % 2) == 0:                                       
        return int(number / 2)                                  
   
    else:                                                       
        return int( (number * 3) + 1)                           


number = int (input("Please enter a positive integer:"))        

print(number)                                                   
while(number !=1):                                              
        number = formula (number)                               
        print (number)                                          

print(number)                                                   
```
In this program a formula is definied; this checks if the number is even - if even it divides by 2, if not it is odd and therefore it is multiplied by 3 and 1 is added to it.
From this formula numbers are then passed through - each number is printed to the variable and returned as an output at the end of the program.

References:

- Stack Overflow, Python Multiplying all even numbers in a list (2017) - https://stackoverflow.com/questions/39835536/python-multiplying-all-even-numbers-in-a-list (Accessed: February 2021)
- Python Programming.net, If statments python tutorial ( Jan 13th, 2014) - https://pythonprogramming.net/if-statement-python-3-basics-tutorial/ (Accessed: February 2021)
- Dev Community, 3 wats to find if a numbers is odd/even in python ( Aug 27th, 2020) - https://dev.to/vikkyomkar/3-ways-to-find-if-a-number-is-odd-even-in-python-1ao7 (Accessed: February 2021) 
- Youtube, Collatz Sequence Algorithm in Python! ( May 8, 2020) - https://www.youtube.com/watch?v=lAp_5qTdOhM (Accessed: February 2021)
- Stack overflow - Making a collatz program automate the boring stuff (2016) -https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff (Accessed: February 2021)
- Automate the boring stuff, Al Sweigart, - Collatz - pg 77 - http://files.urpdfs.com/automate-the-boring-stuff-with-python.pdf (Accessed: February 2021)




<br/>

# Task 4  - Weekday


> File - [weekday.py](https://github.com/andrewbeattycourseware/pands-problems/blob/master/weekday.py)

> Objective - Write a program that outputs whether today is a weekday or not.

> Input - Any day of the week - for example Monday

> Output - For the weekdays; " Yes, unfortunately today is a weekday.", for the Weekend days; " It is the Weekend, Yay!".


## Code:

```ruby
import datetime                                                                           
weeknumber = datetime.datetime.today().weekday()

week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday")      


def whichdayisit (weekday):                                                               
    
    for weekday in range (0,4):                                                           
        return ("Yes, unfortunately it's a weekday")                                      

    else:                                                                                 
        for weekday in range (5,6):                                                                               
            return ("It is the weekend, yay!")                                            


day = input ("Please enter a day of the week: ")                                          
print (whichdayisit (day))                                                                
```
In this program the user is asked to input a day and it returns if it is a weekend or not. The program workds from a predefined formula, which uses the imported datetime module.


References:

- Pythonic.com, Weekday Function in Python (2020) - https://pythontic.com/datetime/date/weekday (Accessed: March 2021)
- Stack Overflow, How to find current day is weekday or weekends in Python? Duplicate, (2015) - https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python (Accessed: March 2021)
- Docs.python.org, date.weekday function, datetime- Basic data and time types (No Date) - https://www.saltycrane.com/blog/2009/04/how-reverse-words-sentence-using-python-and-c/ (Accessed: March 2021)
- Github Gist, Python Weekend Checker (2015) - https://gist.github.com/patrickbeeson/e7e848e3398f287c86ea (Accessed: March 2021)
- Youtube, Python:datetime.date (2016) - https://www.youtube.com/watch?v=nLaq7phtsUU (Accessed: March 2021)
- Codespeedy, Fine the day of week with a given date in python (No Date) - https://www.codespeedy.com/find-the-day-of-week-with-a-given-date-in-python/ (Accessed: March 2021)


<br/>


# Task 5 - Square Root


> File - [Squareroot.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/squareroot.py)

> Objective - Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

> Input - 14.5

> Output - 3.8


## Code:

```ruby
def squareRoot (number):                 
    x=float(number)                      
    y=1.000000                           
    e=0.000001                           
    while x - y > e:                     
          x = (x + y) / 2                
          y = number/x                   
    print (round(x,2))                   

number = input('enter the number : ')    
squareRoot (float(number))               
```

.


References:

- Youtube, Square root of any number instantly - shortcut math (May 6th, 2016) - https://www.youtube.com/watch?v=PJHtqMjrStk (Accessed: March 2021)
- GeeksforGeeks.org, Find root of a number using Newton’s method (May 18th, 2020) - https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N. (Accessed: March 2021)
- Stack Overflow, Square root without pre-defined function in python (2018) - https://stackoverflow.com/questions/46183020/square-root-without-pre-defined-function-in-python (Accessed: March 2021)
- Stack Overflow, Limiting floats to two decimal points (2009) - https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points (Accessed: March 2021)
- Sololearn.com, How can we calculate square root without using any built-in function in python? (April 5, 2020) https://www.sololearn.com/Discuss/2228331/how-can-we-calculate-square-root-without-using-any-built-in-function-in-python (Accessed: March 2021)
- Stack Overflow, Finding square root without using sqrt function? (2014) https://stackoverflow.com/questions/19611198/finding-square-root-without-using-sqrt-function (Accessed: March 2021)

<br/>


# Task 6  - ES (Read for E's)


> File - [es.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/es.py)

> Objective - Write a program that reads in a TXT file and output the number of "e"'s it contains

> Input - Ulysses by James Joyce

> Output - 141150


## Code:

```ruby
import sys                         

with open (sys.argv[1]) as f:       
    data = f.read()                 
    freq = data.count("e")          
    print (freq)                   


## Run file by python typing >  es.py Ulysses.txt  < the in command line ##
```
This program uses the imported System module to access outside files, it then accesses a txt document containing Ulysses by James Joyce. The txt.file is reviewed for "e"'s and the number of "e"'s is returned to the user.

References:

- Gutenberg.org, The Project Gutenberg eBook of Ulysses, by James Joyce (Dec 27, 2019) - https://www.gutenberg.org/files/4300/4300-0.txt (Accessed: April 2021)
- Stack Overflow, Counting specific letters or symbols in a text file in Python (2014) - https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python (Accessed: April 2021)
- Python Examples, Python – Count Number of Characters in Text File (No Date) - https://pythonexamples.org/python-count-number-of-characters-in-text-file/ (Accessed: April 2021)
- Geeks for Geeks, Count the number of times a letter appears in a text file in Python (Nov 25, 2020)   https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ (Accessed: April 2021)
- Tutorialspoint, Python - Command line arguments (No Date) - https://www.tutorialspoint.com/python/python_command_line_arguments.htm (Accessed: April 2021)
- Python Docs, System Specific Parameters and Functions (No Date) - https://docs.python.org/3/library/sys.html (Accessed: April 2021)

<br/>


# Task 7  - Plot Task


> File - [plottask.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/plotTask.png)

> Objective - Write a program that displays a plot of functions

> Input - Functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes

> Output -  

![alt text](https://github.com/VCurry20/-pands-problem-sheet/blob/main/plotTask.png) 


## Code:

```ruby
import matplotlib.pyplot as plt                                                         
import numpy as np                                                                      


fplot= np.array(range(0,4))                                                             
gplot= fplot * fplot                                                                    
hplot= fplot * fplot * fplot                                                            
 
plt.plot(hplot, label='Line H', color='#6495ED', linewidth=4)                           
plt.plot(gplot, label='Line G', color='#40E0D0', linewidth=4, linestyle=':')            
plt.plot(fplot, label='Line F', color='#9FE2BF', linewidth=4, linestyle=':')           

plt.title('Task Week 8', fontsize= 16)                                                  
plt.xlabel('X Axis')                                                                    
plt.ylabel('Y Axis')                                                                    
plt.legend()                                                                           

plt.gca().spines['top'].set_visible(False)                                              
plt.gca().spines['right'].set_visible(False)                                            

plt.text(2.25,20, 'Line H')                                                             
plt.text(2.3,8, 'Line G')                                                              
plt.text(2.6,4, 'Line F')                                                               

# plt.show ()                      

plt.savefig("plotTask.png")      

```

.


References:

- Info Please, Behold the Power of Exponents (No Date) - https://www.infoplease.com/math-science/mathematics/algebra/behold-the-power-of-exponents (Accessed: April 2021)
- Math Works, How to created plot with three lines, (Feb 15, 2015) - https://uk.mathworks.com/matlabcentral/answers/178523-how-to-created-plot-with-three-lines (Accessed: April 2021)
- Andrew Beatty, Lab week 8 / Question 5 - write a program y = x2 ( March 4, 2021) - https://learnonline.gmit.ie/pluginfile.php/306744/mod_label/intro/Lab%2008%20matplotlb.pdf (Accessed: April 2021)
- Stack Overflow, How to make matplotlib graphs look professionally done like this? [closed] (2015) https://stackoverflow.com/questions/24547047/how-to-make-matplotlib-graphs-look-professionally-done-like-this (Accessed: April 2021)
- Towards Data Science, Simple ways to improve your matplotlib ( Aug 14, 2019) https://towardsdatascience.com/simple-ways-to-improve-your-matplotlib-b64eebccfd5 (Accessed: April 2021)
- HTML Coloe Codes, Get HTML color codes, Hex color codes, RGB and HSL values with our color picker, color chart and HTML color names. Let's go! (No Date) https://htmlcolorcodes.com/ (Accessed: April 2021)
- Towards Data Science, 10 tips to improve your plotting (Sept 25, 2019)   https://towardsdatascience.com/10-tips-to-improve-your-plotting-f346fa468d18 (Accessed: April 2021)
- Python informer, Line plot styles in Matplotlib (March 7, 2019) https://www.pythoninformer.com/python-libraries/matplotlib/line-plots/#:~:text=You%20can%20set%20the%20width,style%20using%20the%20linestyle%20parameter. (Accessed: April 2021)
- Queirozf.com, Add Labels and Text to Matplotlib Plots: Annotation Examples (Oct 10, 2020) https://queirozf.com/entries/add-labels-and-text-to-matplotlib-plots-annotation-examples (Accessed: April 2021)
- Uk Math Works, Add Title and Axis Labels to Chart (No Date) https://uk.mathworks.com/help/matlab/creating_plots/add-title-axis-labels-and-legend-to-graph.html (Accessed: April 2021)


<br/>

# Task 8 - Read Me File


> File - Readme.md

> Objective - Outline the Tasks - Code, Aim, and References


References:
- Github Docs, Basic Writing and Formatting Syntax (No Date) https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax (Accessed: April 2021)
- Github guides, Mastering Markdown (No Date) https://guides.github.com/features/mastering-markdown/ (Accessed: April 2021)
- Github Docs, About Readmes (No Date) https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes  (Accessed: April 2021)
- Github Docs, Creating and Highlighting code blocks (No Date) https://docs.github.com/en/github/writing-on-github/creating-and-highlighting-code-blocks (Accessed: April 2021)
- Github, Adam P, Markdown CheatSheet (May 29, 2017) https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet (Accessed: April 2021)
- Stack Overflow, GitHub relative link in Markdown file (2012) https://stackoverflow.com/questions/7653483/github-relative-link-in-markdown-file (Accessed: April 2021)
- Stack OVerflow, How to add images to README.md on GitHub? (2013) https://stackoverflow.com/questions/14494747/how-to-add-images-to-readme-md-on-github (Accessed: April 2021)
