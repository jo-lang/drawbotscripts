
# ----------------------
#  settings 

pw = ph = 500
amount = 5
stroke_w = 20

margin = stroke_w * sqrt(2)
y_size = (pw - 2*margin) / (amount)

# ----------------------
#  function(s) 

def y_shape(pos, s, rot ):
    x, y = pos
    with savedState():
        translate(x + s/2, y + s/2)
        rotate(rot)
        for i in range(3):
            line( (0, 0), (   0, -s/2) )
            line( (0, 0), ( s/2,  s/2) )
            line( (0, 0), (-s/2,  s/2) )
    
# ----------------------
#  drawing 

newPage(pw, ph)
translate(margin, margin)
fill(None)
strokeWidth( stroke_w )
stroke(0, 0.65, 0)

for x in range( amount ):
    for y in range( amount ):
        # rot = choice([0, 90, 180, 270])
        rot = 90 - x * 90 - y * 90
        y_shape( (x * y_size, y * y_size), y_size, rot)

        
# saveImage('rotating_Y.jpg')