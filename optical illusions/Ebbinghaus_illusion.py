# --------
# settings
pw, ph = 900, 500

dia = pw/10
radius_l = ph/3.6
dia_l = ph/3.8

radius_s = ph/7
dia_s = ph/12

# --------
# drawings

newPage(pw, ph)
translate(pw/4, ph/2)

# left side 
fill(1, .5, 0)
oval(-dia/2, -dia/2, dia, dia)

fill(0, .5, .7)
for i in range(6):
    x = cos(2*pi/6 * i) * radius_l
    y = sin(2*pi/6 * i) * radius_l
    oval(x-dia_l/2, y-dia_l/2, dia_l, dia_l)
    
# right side 
translate(pw/2, 0)

fill(1, .5, 0)
oval(-dia/2, -dia/2, dia, dia)

fill(0, .5, .7)
for i in range(8):
    x = cos(2*pi/8 * i + pi/2) * radius_s
    y = sin(2*pi/8 * i + pi/2) * radius_s
    oval(x-dia_s/2, y-dia_s/2, dia_s, dia_s)
    
# saveImage('imgs/ebbinghouse.png')