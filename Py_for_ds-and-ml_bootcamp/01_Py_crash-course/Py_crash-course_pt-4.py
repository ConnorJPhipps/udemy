# Examples from section 4 of the Python for DS and ML Bootcamp on Udemy

def times_2(num):
    return num*2
print(times_2(5))

# Map iterative function application
tmp_list = list(range(5))
# Uses map and converts the output to a list prior to printing
print(list(map(times_2,tmp_list)))

# Lambda expression (Like a cleaned up function. Good for small things you don't want a whole function for.)
# General structure: Input vars on left of : followed by function/action
t_2 = lambda num:num*2
print(list(map(t_2,tmp_list)))

# Lambda expressions do not need to be saved to a var for application
print(list(map(lambda num:num*2,tmp_list)))

# Filter is similar to map but returns values based off a condition (more like an if statement than a loop)
print(list(filter(lambda num: num%2 == 0, tmp_list)))

# Looping through lists of lists
list_of_lists = [[1,2],[3,4],[5,6]]
for a,b in list_of_lists:
    print('{} and {}'.format(a,b))