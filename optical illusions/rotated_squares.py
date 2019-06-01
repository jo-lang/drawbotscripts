
pw = ph = 1000

base_radius = 84
base_amount = 12
sq_size = 27
r_angle = 20
circles = 5

newPage(pw, ph)

fill(.4, .4, 1.0)
rect(0, 0, pw, ph)

translate(pw/2, ph/2)
rotate(90)

fill(None)
strokeWidth(3.5)
stroke(0)

for i in range(1, circles + 1):
    
    radius = i * base_radius
    amount = i * base_amount
    
    for sq in range(amount):
        stroke(0) if sq % 2 == 0 else stroke(1)
        angle = 2 * pi / amount * sq
        x = cos(angle) * radius
        y = sin(angle) * radius
        with savedState():
            translate(x, y)
            rotate(degrees(angle) - r_angle)
            rect(-sq_size/2, -sq_size/2, sq_size, sq_size)
    r_angle *= -1
        
# saveImage('optical_illustion.png')