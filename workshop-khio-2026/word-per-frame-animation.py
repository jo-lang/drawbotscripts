

# assign some text to the 'txt' variable 

txt = 'The continent of modern creation is not only discovered, but it already figures on various maps. Isms are the countries of the spiritual map, each one with a border separating it from the others as in a school geography -- and like everything in school books right and wrong at the same time. For today the borderlines between isms are beginning to be obscured. And what interest us are not so much the surrounding constructions as the matter itself, the individual achievement which stands finally behind collective theories. In my opinion, for the sake of honesty, no new ism should be created.'


# assign some values to the 'PW' and 'PH' variables
PW = 1920
PH = 1080

# iterate througth the text which is split at every space. 
for word in txt.split(' '):
    # make a new page for every word
    newPage(PW, PH)
    # select a font from all installed fonts 
    font(choice(installedFonts()))
	# define a fontsize with a value between 140 and 330
    fontSize(randint(140, 330))
    # draw the word center aligned 
    text(word, (PW/2, PH*.45), align ='center')


# you can uncomment the next line drawbot will save an mp4 movie where each page is a frame. 
# saveImage('word-per-frame-animation.mp4')