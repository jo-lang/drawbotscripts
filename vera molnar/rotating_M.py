# --------------
#  settings 

pw = ph = 500
amount = 7
stoke_w = 4

cell_s = pw / (amount + 2)

# --------------
#  function(s)

def M(pos, s, angle):
    x, y = pos
    with savedState():
        translate(x, y)
        rotate(angle)
        polygon(
            (-s/2, -s/2),
            (-s/2,  s/2),
            (   0,    0),
            ( s/2,  s/2),
            ( s/2, -s/2),
            close = False)
         
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
        rot = -90 - x * 90 - y * 90
        M((x * cell_s, y * cell_s), cell_s, rot)
        
# saveImage('rotating_M.jpg')