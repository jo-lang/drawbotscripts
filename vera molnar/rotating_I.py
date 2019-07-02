# --------------
#  settings 

pw = ph = 500
amount = 20
stoke_w = 1

cell_s = pw / (amount + 2)

# --------------
#  function(s)

def I(pos, s):
    x, y = pos
    with savedState():
        translate(x, y)
        if random() > .5:
            rotate(randint(-30, 30))
        elif random() > .75:
            rotate(randint(80, 110))
        else:
            rotate(randint(-8, 8))
            
        line((-s/2, s/2),(-s/2,-s/2))
        line(( s/2, s/2),( s/2,-s/2))
        line((-s/2,   0),( s/2,   0))

# --------------
#  drawings 

newPage(pw, ph)
translate(cell_s * 1.5, cell_s * 1.5)

fill(None)
stroke(0)
strokeWidth(stoke_w)
lineJoin('bevel')
lineCap('square')

for x in range(amount):
    for y in range(amount):
        I((x * cell_s, y * cell_s), cell_s)
        
# saveImage('rotating_I.jpg')