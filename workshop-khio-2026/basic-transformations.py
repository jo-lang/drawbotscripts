
# define the variable 'txt' and assign some text to it
txt = 'The continent of modern creation is not only discovered, but it already figures on various maps. Isms are the countries of the spiritual map, each one with a border separating it from the others as in a school geography -- and like everything in school books right and wrong at the same time. For today the borderlines between isms are beginning to be obscured. And what interest us are not so much the surrounding constructions as the matter itself, the individual achievement which stands finally behind collective theories. In my opinion, for the sake of honesty, no new ism should be created.'


# split the value of the 'txt' variable (the text) at every period ('.') assign the list to the 'sentences' variable 
sentences = txt.split('.')


# make a new A3 page 
newPage('A3')

# move the origin to the center of the page 
translate(width()/2, height()/2)

# rotate the coordinate system counter clock wise by 15 degrees 
rotate(15)
# mirror the coordinate system on the x axis 
scale(-1, 1)
# skew the coordinate system by 30 degrees 
skew(30)


# set the font size to 21 
fontSize(21)

# define the variable 'x' and set it to 100
x = 100

# define the variable 'angle' and set it to 5
angle = 5

# iteratoe through the values of the sentences variable (in our case it is the text split at the periods)

for sentence in sentences: 
    # split each sentence at every space and iterate through the result  
    for word in sentence.split(' '):
        # draw each word at the position of 'x' and zero
        text(word, (x, 0))
        # after rotate the coordinate system by the value of the 'angle' variable
        # this is done several times (as many times as there are words)
        rotate(angle)
        # increalse the value of the 'x' variable 
        x += 4
    # after drawing all word of the current sentence increase the value of 'x' by a 100
    x = 100
    # move the origin 300 pixels to the left
    # this is not left of the page but left of however the coordinate system is currently rotated. 
    # a mix of rotations and translations can be quite confusing! 
    translate(300, 0)


