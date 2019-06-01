
# Müller Lyer Illusion 
pw = ph = 400 # define varaibles to set width and height of the canvas
cols = 20 # define how many columns there should be 
rows = 10 # define how many rows there should be 
frames = 30 # define how many frames the gif should have. more pages mean slower movement

angle_diff = 2 * pi/frames # we want the loop to be make one full circle. 2 times pi is 306. Divided by the amount of pages this gives us the angle difference between pages. 

gap = pw/(cols+1) # calculate the gap between the lines. 
l   = (ph - 2 * gap)/rows # calculate the length of the line. 

for f in range(frames): 
    newPage(pw, ph)
    translate(gap, gap)
    fill(None)
    strokeWidth(2)
    for x in range(cols):
        y_off = cos( 3 * pi * x/cols + angle_diff * f ) * gap/2 # calculate how high or low the arrowhead should be 
        for y in range(rows+1):
            stroke(1,0 ,0) if y % 2 == 0 else stroke(0, 0, 1)
            if y < rows:
                line((x*gap, y*l), (x*gap, y*l+l))
            stroke(0)
            y_off *= -1 # switch to change direction 
            line( (x*gap, y*l), (x*gap - gap/2, y*l - y_off) )
            line( (x*gap, y*l), (x*gap + gap/2, y*l - y_off) )

# saveImage('~/Desktop/opti_illu2.gif')