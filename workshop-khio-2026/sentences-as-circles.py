
# assign some text to the variable 'txt' 

txt = 'The continent of modern creation is not only discovered, but it already figures on various maps. Isms are the countries of the spiritual map, each one with a border separating it from the others as in a school geography -- and like everything in school books right and wrong at the same time. For today the borderlines between isms are beginning to be obscured. And what interest us are not so much the surrounding constructions as the matter itself, the individual achievement which stands finally behind collective theories. In my opinion, for the sake of honesty, no new ism should be created.'

# split the text at every period followed by a space to turn it into a list of sentences and assign this list to the variable sentences 
sentences = txt.split('. ')

# make a new page 
newPage('A3')

# move the origin (0, 0) to the center and top of the page 
translate(width()/2, height()- 40)
# set the font size 
fontSize(21)

# try different values for the next three variables.
# radius is the distance of each word from the center of the circle  
radius = 100
# y_shift is the gap between the circle centers 
y_shift = -200
# angle is the angle between each word 
angle = -5

# iterate through the sentences 
for sentence in sentences: 
    # save the current state of transformations. 
    # every change inside the 'savedState()' will be 'forgotten' 
    with savedState():
        # rotate(90)
        # split the current sentence at every wordspace and iterate througth the result
        for word in sentence.split(' '):
            # draw each word 
            text(word, (radius, 0))
            # and rotate the coordinatesystem by value of the 'angle' variable 
            rotate(angle)
    # after drawing each sentence shift the origin by the value of the 'y_shift' variable 
    translate(0, y_shift)


