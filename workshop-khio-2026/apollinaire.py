
# After the artwort “Il Pleut” (It’s Raining) by Guillaume Apollinaire, 1918.
# https://www.moma.org/interactives/exhibitions/2012/inventingabstraction/?work=17
# ------------------


# assigning some text to the variable 'txt'

txt = ' Il pleut des voix de femmes comme si elles étaient mortes même dans le souvenir c’est vous aussi qu’il pleut merveilleuses rencontres de ma vie ô gouttelettes et ces nuages cabrés se prennent à hennir tout un univers de villes auriculaires écoute s’il pleut tandis que le regret et le dédain pleurent une ancienne musique écoute tomber les liens qui te retiennent en haut et en bas'


# making a new page 
newPage('A4')

# setting a font 
font('MinionPro-Bold')
# moving the origin (0, 0) to the top left of the page 
translate(0, height()-20)

# defining the variables 'x' and 'y' and setting them to 0
x, y = 0, 0 

# iterating througth all the letters of the text 
for c, char in enumerate(txt):
    # drawing the letter (char)
    text(char, (x, y))
    # increase the value of x 
    x += random() * 3
    # decrease the value of y
    y -= 10
    
    # if 'y' is so small that it does not fit on the page reset it to 0 and decreseas 'x'
    if y < (-height()+40):
        y = 0
        x -= random()*80
