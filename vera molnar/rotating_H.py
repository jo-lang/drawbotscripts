# --------------
#  settings 

pw = ph = 500
amount = 24
factor = 1/3
regular = False

cell_s = pw / (amount + 2)

# --------------
#  function(s)

def I(pos, s):
    x, y = pos
    polygon(
        (-s/2, -s/2),
        (-s/2, +s/2),
        (-s/2 * factor, +s/2),
        (-s/2 * factor, +s/2 * (1 - factor)/2),
        (+s/2 * factor, +s/2 * (1 - factor)/2),
        (+s/2 * factor, +s/2),
        (+s/2, +s/2),
        (+s/2, -s/2),
        (+s/2 * factor, -s/2),
        (+s/2 * factor, -s/2 * (1 - factor)/2),
        (-s/2 * factor, -s/2 * (1 - factor)/2),
        (-s/2 * factor, -s/2),
    )

# --------------
#  drawings 

newPage(pw, ph)
translate(cell_s * 1.5, cell_s * 1.5)

for x in range(amount):
    for y in range(amount):
        with savedState():
            translate(x * cell_s, y*cell_s)
            if regular:
                if (x + y) %2: rotate(90)
            else:
                if random() > .5: rotate(90)
            I((0, 0), cell_s)
        
# saveImage('rotating_H.jpg')