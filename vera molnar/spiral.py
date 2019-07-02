
pw = ph = 500
s = 5

amount = int(pw / s + 4)

newPage(pw, ph)
translate(pw/2, ph/2)

rect(-s, 0, s, s)

for i in range(amount):
    rect(0, 0, s*i, s)
    rotate(-90)
    translate(0, s * (i-1))
    
# saveImage('spiral.jpg')