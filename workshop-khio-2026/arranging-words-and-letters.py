

# assign some text the the variable 'txt'

txt = 'The continent of modern creation is not only discovered, but it already figures on various maps. Isms are the countries of the spiritual map, each one with a border separating it from the others as in a school geography -- and like everything in school books right and wrong at the same time. For today the borderlines between isms are beginning to be obscured. And what interest us are not so much the surrounding constructions as the matter itself, the individual achievement which stands finally behind collective theories. In my opinion, for the sake of honesty, no new ism should be created.'



# make a new page 
newPage('A4')

# iterate througth all characters of the text 
for char in txt:
    # draw each character at a random position on the page 
    # random() will produce any value between 0 and 1 (eg 0.11235, 0.67237, 096234)
    # width() will get the width of the current page and height() will get the height 
    # multiplying the random value and the widht/height will give any value between 0 and the maxium width/height 
    text(char, (random()*width(), random()*height()))



# make another page 
newPage('A4')

# iterate through all characters of the text 
# with enumerate you can get the index (a number which is the position of the element in the whole) and the elemente 
# in this case 'c' will be the index and 'char' will be the character 
for c, char in enumerate(txt):
    # give each character a new fill color (the first one will be the darkest, the last one almost white)
    # this is done by dividing 'c' by the length of the whole text
    # the length of the whole text can be found with the 'len()' function.
    # in this case it is 391 characters, so c (0, 1, 2, ..., 389, 390, 391) is divided by 391 
    # when there is only one value in 'fill()' is is grayvalue (0 being black and 1 being white)
    fill(c/len(txt))
    # now draw that character with the new fill color anywhere on the page 
    text(char, (random()*width(), random()*height()))



# make another page 
newPage('A4')

# assigning a list of all fonts to the 'all_font' variable 
all_fonts = installedFonts()

# iterating through the text and placing each letter at a random position on the page 
for letter in txt:
    fill(random(), random(), 1)
    fontSize(random()*38)
    font( choice(all_fonts)  )
    text(letter, (random()*width(), random()*height() ) )
    


# make another page     
newPage('A4')

# define the variables 'x' and 'y' and set both of them to zero 
x = 0
y = 0

# move the origin to the left, top (minus some pixels) of the page 
translate(0, height()-30)

# iterate through the text 
for char in txt:
    # draw the text at the current values of 'x' and 'y' 
    text(char, (x, y))
    
    # increase the 'x' value by a random value. 
    # randint(4, 8) will give either 4, 5, 6, 7 or 8
    x += randint(4, 8)
    # increase or decrease the 'y' value by a random value between -4 and 4
    # randint(-4, 4) will give any value of -4, -3, -2, -1, 0, 1, 2, 3, 4
    # multiplying this value by 'random()' mean it will be anywhere between that and zero 
    y += randint(-4, 4)*random()
    
    # if the value of 'x' is bigger than the width or the page reset the 'x' to 'zero' and decrease the 'y' value by 50
    if x > width():
        x = 0 
        y -= 50


# make another page 
newPage('A4')
fontSize(40)

# defining and a variable 'x' and a variable 'y' to use later 
x = 20
y = 20

# defining the variable 'x_dist' to use later for the gap between the letters
x_dist = 17
y_dist = 2

# iterating through the text 
for l, letter in enumerate(txt):
    # draw the letter at the x and y position 
    text(letter, (x, y))

    # if the value of x is greater than the width of the page reset it to 20 
    if x > width():
        x = 20
    # if the letter is an 'e' than change the fontSize
    if letter == 'e':
        fontSize(random()* 24)
    # if the letter is an 'a' than change the fillcolor
    elif letter == 'a':
        fill(random(), random(), 0)

    # increase the value of x by the value of the 'x_dist' variable
    x = x + x_dist
    # increase the value of y by the value of the 'y_dist' variable
    y += y_dist






# make a new page     
newPage('A4')

# define the variables 'x' and 'y' and set both of them to zero 
x = 0
y = 0

# move the origin to the left, top (minus some pixels) of the page 
translate(0, height()-30)


# split the text at every space and iterate through the elements 
for word in txt.split(' '):

    # set the font size to something between 10 and 18    
    fontSize(randint(10, 18))
    # draw the word at the current values of 'x' and 'y' 
    text(word, (x, y))

    # increase 'x' by some random value     
    x += randint(40, 80)
    # increase or decrease the 'y' value by a random value between -4 and 4
    y += randint(-4, 4) *random()
    
    # if the value of 'x' is bigger than the width or the page reset the 'x' to 'zero' and decrease the 'y' value by 50
    if x > width():
        x = 0 
        y -= 50



 
# make a new page     
newPage('A4')

# define the variables 'x' and 'y' and set both of them to zero 
x = 0
y = 0

# define the variable 'l_height' and set its value to 12
l_height = 12

# define the variable 'fnt_s_factor' and set its value to 1.05
fnt_s_factor = 1.05

# define the variable 'fnt_s' and set it to 10. 
fnt_s = 10
# move the origin 20 pixels to the left and to the top of the page minus 30 pixels
translate(20, height()-30)

# split the text at every space and iterate througth the elements

for text_seg in txt.split(' '):
    # the the font size to the value of the variable 'fnt_s'
    fontSize(fnt_s)
    # draw the text element at the current value of 'x' and 'y'
    text(text_seg, (x, y))
    
    # increase 'fnt_s' by multiplying it with the value of 'fnt_s_factor' 
    fnt_s *= fnt_s_factor
    # decrease 'y' with the value by the 'l_height' variable 
    y -= l_height
        
        


# adding another page 
newPage('A4')
fontSize(24)

# define the variable 'max_font_size' and set it to 24
max_font_size = 24
# define the variable 'y' and set it to the height of the page minus the value of the 'max_font_size' variable 
y = height() - max_font_size

# iterating througth the text which is split into fragments whenever there is an 'o'
for fragment in txt.split('o'):
    # for every fragment of the split text make a new font size 
    fontSize(random()*max_font_size)
    # draw the fragment at 20 and the value of the 'y' variable
    text(fragment, (20, y))
    # decrease the value of 'y'
    y -= max_font_size






# make a new page     
newPage('A4')

# define the variables 'x' and 'y' and set 'x' to 10 and 'y' to 0
x = 10
y = 0


line_height = 12

# define the 'split_chars' variabel and assign some letters to it
# in this case it is a list of some of the most frequently used letters in english 
split_chars = 'etaoinshrdlu'

# move the origin to the top of the page minus some margin of 30
translate(0, height()-30)

# the next few lines are a loop inside a loop 

# iterate through the letters of the 'split_chars' variable 
for split_char in split_chars:
    # for each one of the letters split the whole text of the 'txt' variable at that letter
    # and iterate througth the list of text segmente of that split 
    for text_seg in txt.split(split_char):
        # draw the text segment the the current 'x' and 'y' value
        text(text_seg, (x, y))
        # decrease the value of 'y' by the value of the 'line_height' variable
        y -= line_height
    # after the inner loop the value of 'y' as reset to zero
    y = 0 
    # and the value of x is increased by a calculated value
    # the value for the x shift is caluclated by dividing the full width of the page by the length of the split_chars variable. 
    # This is the amount of times that the full text is split into text segments. 
    x += width()/len(split_chars)


