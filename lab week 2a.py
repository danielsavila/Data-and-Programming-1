#LAB 1
#### fix the following errors!
#### do not use any web-based resources to figure them out

#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list_len)

#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c', 'd']
z[3] = 'd'

#5 run all these lines at once. why does the x not display 10, 
#followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
blue = 'blue'
color = 'My favorite color is %s, what is yours?' % blue
print(color)

#7
yellow = 'yellow'
color = 'My favorite color is {}, what is yours?'.format(yellow)
print(color)

#8
red = 'red'
color = f'My favorite color is {red}, what is yours?'
print(color)

#### answer the following questions by adding lines, but without changing the code given

#9 make the entries in this list unique
schools = ('harris', 'booth', 'crown', 'harris', 'harris')
schools = {'harris', 'booth', 'crown', 'harris', 'harris'}
print(schools)

#10 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals = ['bird', 'horse', 'dog', 'fish']
animals[2] = 'cat'
print(animals)

#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'All that snow we had this winter sure was fun!'
my_sent = my_sent.lower()
list = [my_sent[0:3], my_sent[4:8], my_sent[9:13], my_sent[14:16], my_sent[17:20], my_sent[21:25], my_sent[26:32], my_sent[33:37], my_sent[38:41], my_sent[42:45]]
print(list)


#Lab 2!
#NAMES
#Unless otherwise noted, try solving these using class content and without searching online

#1
#Modify this code so that when i is 5 it doesn't print anything (including Finished!)
#and instead moves directly onto 6, while leaving it unchanged for other values of i

i = 0
while i < 10:
    if i < 5:
        print('little')
    elif i == 5:
        i += 1
        continue
    elif i >= 5:
        print('big')
    else:
        print('what happened?')
    print('Finished!')
    i += 1

#2
#Write a for loop that prints this pattern:
#HINT: you can write a for-loop inside of a for-loop

#1
#1 2
#1 2 3
#1 2 3 4
list = [1, 2, 3, 4]
second_list = []
for val in list:
    second_list.append(val)
    print(second_list)


#3
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]  
#NOTE:  The spacing is just to show which numbers are converted to which
#HINTS: There are three steps here: mapping, filtering, and flattening the nested lists
#       Try doing this in a for-loop, then try doing it in a list comprehension
#       You may need to check StackOverflow for how to flatten a nested list


# using a for loop
# note that I found the modulo/remainder operator after looking up from ChatGPT,
# have seen from previous python experience.

for item in start_list:
    for i in range(len(item)):
        if item[i] == 2:
           item[i] = 1
        elif item[i] == 4:
           item[i] = 2
        elif item[i] == 6:
           item[i] = 3
        elif item[i] == 8:
           item[i] = 4
print(start_list)


# attempt at using a list comprehension
for item in start_list:
    updated_list = [item[i] / 2 for i in range(len(item)) if item[i] % 2 == 0]
print(updated_list)

# not sure why the list comprehension is not working here...


#4
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}
#HINTS: The datetime library has a function that turns strings of the right format into dates
#       Again, start with a for-loop, but make a dictionary comprehension in the end

