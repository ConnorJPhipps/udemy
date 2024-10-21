# Examples from section 4 of the Python for DS and ML Bootcamp on Udemy

# Initializing numeric ascending lists
tmp_list = list(range(10))
print(tmp_list)

# List comprehension
# General structure is desired output prior to writing the loop
[print(num**2) for num in tmp_list]

# Method/Function
def my_method(message):
    print(message)

my_method('hello')

def default_test(message='test'):
    print(message)
default_test()