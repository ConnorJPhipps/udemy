#!/usr/bin/env python
# coding: utf-8
from soupsieve.util import lower

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/?couponCode=PY20)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.
print("** What is 7 to the power of 4?**")
print(7^4)

print("** Split this string:**")
s = "Hi there Sam!"
print(s)
print(s.split())

planet = "Earth"
diameter = 12742
print("** Given the variables: {}, {}**".format(planet, diameter))
print("** Use .format() to print the following string: **")
print("The diameter of Earth is 12742 kilometers.")
print("The diameter of {} is {} kilometers.".format(planet, diameter))

print("** Given this nested list, use indexing to grab the word 'hello' **")
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst)
print(lst[3][1][2][0])

print("** Given this nested dictionary grab the word 'hello'. Be prepared, this will be annoying/tricky **")
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d)
print(d['k1'][3]['tricky'][3]['target'][3])

print("** What is the main difference between a tuple and a list? **")
print("Lists can be changed, tuples are immutable.")

print("** Create a function that grabs the email website domain from a string in the form: **")
def get_email_website(email_address):
    print(email_address.split("@")[-1])
get_email_website("user@domain.com")


print("** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **")
def check_for_dog(test_string):
    if "dog" in lower(test_string):
        print("True")
check_for_dog('Is there a dog here?')
check_for_dog('Is there a DOG here?')

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
count_dog_str = 'This dog runs faster than the other dog dude!'
print(len(list(filter(lambda dog_str: "dog" in dog_str.lower(), count_dog_str.split()))))

print("** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**")
seq = ['soup','dog','salad','cat','great']
print(seq)
print(list(filter(lambda word: word[0].lower() == "s", seq)))

print("Final Problem")
print("**You are driving a little too fast, and a police officer stops you. Write a function")
print("   to return one of 3 possible results: 'No ticket', 'Small ticket', or 'Big Ticket'.")
print("   If your speed is 60 or less, the result is 'No Ticket'. If speed is between 61")
print("   and 80 inclusive, the result is 'Small Ticket'. If speed is 81 or more, the result is")
print("   'Big Ticket'. Unless it is your birthday (encoded as a boolean value in the parameters of the function)")
print("   -- on your birthday, your speed can be 5 higher in all cases.**")

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed - 5
    if speed < 61:
        print("'No Ticket'")
    elif speed < 81:
        print("'Small Ticket'")
    else:
        print("'Big Ticket'")
print("Speed: 81, B-day: Yes")
print(caught_speeding(81,True))
print("Speed: 81, B-day: No")
caught_speeding(81,False)
print("Speed: 75, B-day: Yes")
caught_speeding(75, True)