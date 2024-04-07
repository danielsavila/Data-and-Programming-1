# PPHA 30537
# Spring 2024
# Homework 1

# Daniel Avila
# danielsavila

# Due date: Sunday April 7th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.
index_position = 0
list1 = ['a', 'b', 'c', 'd']
list2= range(5)

for i in list2:
    index_position += 1
    print('"The value at position', index_position, 'is', i)

# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

phrase0 = 'A man, a plan, a canal, Panama!'
phrase0 = phrase0.lower().replace(",", "").replace("!", "").replace(" ", "")              # found this documentation on the replace method
phrase0_list = [value for value in phrase0]                                               # https://stackoverflow.com/questions/9452108/how-to-use-string-replace-in-python-3-x
if phrase0_list == phrase0_list[::-1]:
    print("This is a palindrome")
if phrase0_list != phrase0_list[::-1]:
    print("This is not a palindrome")
    
    
phrase1 = 'radar'
phrase1 = phrase1.lower().replace(",", "").replace("!", "").replace(" ", "")            
phrase1_list = [value for value in phrase1]                                              
if phrase1_list == phrase1_list[::-1]:
    print("This is a palindrome")
if phrase1_list != phrase1_list[::-1]:
    print("This is not a palindrome")   
    
    
phrase2 = 'Microsoft'
phrase2 = phrase2.lower().replace(",", "").replace("!", "").replace(" ", "")             
phrase2_list = [value for value in phrase2]                                              
if phrase2_list == phrase2_list[::-1]:
    print("This is a palindrome")
if phrase2_list != phrase2_list[::-1]:
    print("This is not a palindrome")   


phrase3 = "This isn't a palindrome"
phrase3 = phrase3.lower().replace(",", "").replace("!", "").replace(" ", "")              
phrase3_list = [value for value in phrase3]                                              
if phrase3_list == phrase3_list[::-1]:
    print("This is a palindrome")
if phrase3_list != phrase3_list[::-1]:
    print("This is not a palindrome")   



# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.


available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']

while True:
    choice = input('Please pick a vegetable I have available: ')
    var = choice in available_vegetables
    if var == True:
        print("you can have it")
        break
    else:
        print("we dont have those")


# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.

string_list = ["Ah! ", "the ", "big ", "grey ", "fox ", "is ", "blue!"]                                         # referenced chatGPT for format of list comprehension formatting
new_list = [i.lower() for i in string_list if i[0].lower() != 'a' and i[0].lower() != 'b']                      # in both this question and the next
print(new_list)



# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}


short_names = ['IL', 'IN', 'MI', 'WI']                                          # dictionary comprehension reference https://www.freecodecamp.org/news/dictionary-comprehension-in-python-explained-with-examples/
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']                  # and class slides

list_length = range(len(short_names))
dictionary = {short_names[i]: long_names[i] for i in list_length}
print(dictionary)


#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]              

def goldilocks(value):
    b, c = value                                                                # referenced chatgpt for unpacking tuples.
    summation = b + c
    if summation > 10:
        output = "big"
        return output
    elif summation == 10:
        output = "just right"
        return output
    else:
        output = "small"
        return output 
        
new_list = [goldilocks(i) for i in start_list]
print(new_list)
                      

# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.


def my_func(a = 10):
    b = 40
    return a + b
x = my_func()

# the new way enables us to save memory because it limits the amount of global variables the computer needs to store, and
# it enables us to manually change new values for "a" such that we can use my_func() in other scenarios as needed.


# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:


import random

def assign_num_to_char(r_num_gen):
    char_transform = [chr(num) for num in r_num_gen]                                                # documentation on chr() https://www.w3schools.com/python/ref_func_chr.asp
    complete_pswd = ''.join(char_transform)                                                         # join function https://pythonbasics.org/join/
    return complete_pswd

def nu_pswd(pswd_length, special_check = True):
    if int(pswd_length) > 16:
        print("password length is too long!")
        
    elif int(pswd_length) < 8:
        print("password is too short!")
    
    elif special_char == "False" or "false": 
        special_check == False
        r_num_gen_cap = [random.randint(65, 90) for value in range(0, int(pswd_length) // 3)]                 # integer division https://stackoverflow.com/questions/21316968/integer-division-in-python-2-and-python-3
                                                                                                              # used this table to determine characters
        r_num_gen_lower = [random.randint(97, 122) for value in range(0, int(pswd_length) // 3)]              # https://en.wikipedia.org/wiki/List_of_Unicode_characters
        
        r_num_gen_numbers = [random.randint(48, 57) for value in range(0, int(pswd_length) // 3)]
        
        r_num_gen = r_num_gen_cap + r_num_gen_lower + r_num_gen_numbers                                       # adding lists = https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
        
        pswd = assign_num_to_char(r_num_gen)
        return print("Your new password is: ", pswd)
    else: 
        special_check = True
        r_num_gen = [random.randint(33, 126) for value in range(0, int(pswd_length))]
        
        pswd = assign_num_to_char(r_num_gen)
        return print("Your new password is:", pswd)
        
pswd_length = int(input("Enter number of characters for your password: "))
special_char = input("Do you want speical characters? Type (True) or (False): ")
    
nu_pswd(pswd_length, special_char)


# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.

class MovieDatabase:                                                            # used this documentation as reference
    movies = []                                                                 # https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables        
    
    def __init__(self, user_name):
        self.user_name = user_name
    
    def add_movie(self, movie_name, genre, rating):
        self.movie_name = movie_name
        self.genre = genre
        self.rating = rating
        movie = [movie_name, genre, rating]
        self.movies.append(movie)
        
        
    def what_to_watch(self):
        if len(self.movies) == 0:
            print("no movies in the list!")
        else:
            random_number = random.randint(0, len(self.movies) - 1)
            print(self.movies[random_number])


test = MovieDatabase(user_name = "Daniel Avila")
test.add_movie("Bourne Identity", "action", "5")
test.add_movie("Sinbad", "cartoon", "4")
test.add_movie("Buffalo 66", "drama", "5")
test.add_movie("Fitzcarrado", "drama", "3")

test.user_name
test.what_to_watch()
test.movies

# to reset the list, use...
test.movies = []
    

    