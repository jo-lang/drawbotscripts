
# python has some functions that it can do but that are not 'on' by default 
# if we want to use those function we need to import them 
# in our case we want to use the 'seed' function which can be used to always get the same random() values 
# so we import it with the following line 
from random import seed 

# make a new page 
newPage('A4')

# set some value to  the 'seed()' function. this can be any number or a word (eg: seed(123) or seed('word'))
seed(123)

# define the amount variable and set it to 100
amount = 100

# loop through the amount (0, 1, 2, ..., 97, 98, 99)
for i in range(amount):
    # set a new fill color with the red value at random
    fill(random(), .2, .5)
    # set the variable 'dia' to a random value between 30 and 50.
    dia = randint(30, 50)
    # draw a circle anywhere on the page with the previously random generate diameter 
    oval(random() * width(), random() * height(), dia, dia)


