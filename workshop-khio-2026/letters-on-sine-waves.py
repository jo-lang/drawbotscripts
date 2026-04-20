
# make a new page
newPage('A4')


# translate the origin to the bottom center of the page 
translate(width()/2, 0)


# change the values of the next three variables to get differnt results 

# define a variable for a wave length 
wave_l = 360

# define a variable for the base value of the amplitude 
base_amp = 18

# define a variable for the gap between the lines 
y_gap = 4

# assigen some text to the 'txt' variable 
txt = 'lowercaseletters'

# iterate througth the text (assigned to the 'txt' variable)
for c, letter in enumerate(txt):
    # for each letter, go from the bottom the height of the page with a distance of 'y_gap'
    for y in range(0, height(), y_gap):
        # calculate the x position with sinus (sin) and pi
        x = sin(2*pi * ((y%wave_l)/wave_l)) * (c * base_amp)
        # draw the letter at the calculated position
        text(letter, (x, y))
        text(letter, (-x, y))
