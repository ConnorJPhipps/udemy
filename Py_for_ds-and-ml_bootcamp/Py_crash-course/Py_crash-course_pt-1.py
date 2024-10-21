# Examples from section 4 of the Python for DS and ML Bootcamp on Udemy

# Formating strings
num = 7
name = 'Connor'
# Inserts vars by order (like java methods)
net = ('My number is {} and my name is {}'.format(num,name))
print(net)
# Agnostic of order of vars in formated string
net = ('My number is {one} and my name is {two}'.format(one=num,two=name))
print(net)
