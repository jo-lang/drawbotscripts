# Wundt illusion
# --------
# settings 

pw = 500
ph = 900
strokeW = 1.5
stroke_amount = 17


# --------
# drawings 
newPage(pw, ph)
translate(pw/2, 0)
fill(None)
stroke(0, 0, 1)
strokeWidth(strokeW)

for i in range(stroke_amount):
    line((-pw/2, ph/2), (0, ph/(stroke_amount - 1) * i))
    line(( pw/2, ph/2), (0, ph/(stroke_amount - 1) * i))

fill(1, 0, 0)
stroke(None)

rect(-pw/6, ph/8, 4, ph/8 * 6)
rect( pw/6, ph/8, 4, ph/8 * 6)

# saveImage('imgs/wundt_illusion.png')