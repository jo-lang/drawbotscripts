# -------------
#  settings 

pw = ph = 500
st_w = 20
angle = 2

angle_r = radians(angle)
new_s = pw

# -------------
#  drawing  

newPage(pw, ph)
translate(pw/2, ph/2)

while new_s > (2 * st_w):
    
    fill(0)
    rect(-new_s/2, -new_s/2, new_s, new_s)
    new_s -= 2 * st_w

    fill(1)
    rect(-new_s/2, -new_s/2, new_s, new_s)

    new_s = new_s / (sin(angle_r) + cos(angle_r))
    rotate(angle)
    
# saveImage('rotating_square_3.jpg')