
pw = ph = 500
rings = 50
factor = .785
frames = 36

amplitude = 50
frequency = 2

dist = pw/rings

def base_page():
    newPage(pw, ph)
    rect(0, 0, pw, ph)
    translate(pw/2, ph/2)
    fill(None)
    strokeWidth(1)
    stroke(0, 1, 0)

for f in range(frames):

    base_page()

    for r in range(1, rings):
        angle = r / rings * 2 * pi * frequency
        angle -= f/frames * 2 * pi
        y_off = amplitude * cos(angle)

        dia = r * dist
        dia_y = dia * factor
        oval(-dia/2, -dia_y/2 + y_off, dia, dia_y)
        
# saveImage('waves4.gif')