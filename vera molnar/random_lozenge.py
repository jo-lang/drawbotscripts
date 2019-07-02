# --------------
#  settings 

pw = ph = 500
amount = 24

cell_s = pw / (amount + 2)


# --------------
#  function(s) 

def loz(pos, s):
    x, y = pos
    with savedState():
        translate(x, y)
        rotate(choice([0, 90]))
        polygon( (0, -s/2), (s/4, 0), (0, s/2), (-s/4, 0))

# --------------
#  drawings 

newPage(pw, ph)
rect(0, 0, pw, ph)
fill(1)
translate(cell_s * 1.5, cell_s * 1.5)

for x in range(amount):
    for y in range(amount):
        loz((x * cell_s, y * cell_s), cell_s)
        
# saveImage('random_lozenge.jpg')