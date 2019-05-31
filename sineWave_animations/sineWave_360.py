# some basic settings 
ph = 350 # pageheight
pw = ph * 2 # pagewidth
steps = 180 # how many pages / steps to draw
dot_s = 8 # size of the dots at the end of the radius 

radius = ph/2 * .75 
angle = 2*pi/steps 
gap = radius / (steps - 1) * 2 # used to draw the dots of the sine wave 

sin_vals = [sin(i*angle) for i in range(steps)] # calculate and store the sine values once 

def base_page(i):
    '''basic stuff that gets drawn and used on every page'''
    newPage(pw, ph)
    fill(1)
    rect(0, 0, pw, ph)
    fill(0)
    translate(0, ph/2)
    fontSize(8)
    for j in range(-10, 11, 2):
        text('%.1f' % (j/10), (pw/2, radius/10 * j), align = 'right')

    fill(.5)
    rect(ph/2 * .25, -ph/2, 1, ph)
    rect(ph/2 * .25 + 2 * radius, -ph/2, 1, ph)

    # drawing of the sine wave 
    with savedState():
        translate((ph - radius *2)/2, 0)
        for st in range(steps):
            sin_val = sin_vals[ (st+i+1) % steps]
            oval(st * gap - 2, sin_val * radius - 2, 4, 4)

    translate(ph + ph/2, 0)
    fill(None)
    stroke(.5)
    strokeWidth(1)
    oval(-radius, -radius, radius*2, radius*2)
    line((-ph/2 * 3, 0), (ph/2, 0))
    line((0, -ph/2), (0, ph/2))
    fontSize(14)


for i in range(steps):
    base_page(i)
    cos_val = cos(i * angle)
    sin_val = sin(i * angle)
    x = cos_val * radius
    y = sin_val * radius
    
    stroke(.75)
    line((x, max(0, y)),(x, -radius))
    line((max(x, 0), y),(- pw/2 + radius, y))
    
    strokeWidth(2)
    # radius 
    stroke(0, 0, 1)
    line((0, 0),(x, y))
    # cosine distance 
    stroke(1, 0, 0)
    line((0, 0),(x, 0))
    # sine distance 
    stroke(0, .5, 0)
    line((0, 0),(0, y))
    
    stroke(None)

    fill(0, 0, 1, .2)
    pth = BezierPath()
    pth.moveTo((0, 0))
    pth.lineTo((radius/4, 0))
    pth.arc((0, 0), radius/4, 0, degrees(i * angle), clockwise = False)
    pth.closePath()
    drawPath(pth)


    fill(0)
    text('cos(θ)', (x/2, -18), align = 'center')
    text('sin(θ)', (8, y/2 + 4))
    text('%d°' % (i * degrees(angle)), (radius/4 + 4, 8))    
    text('%.3f' % cos_val, (x, -radius - 16), align = 'center')
    text('%.3f' % sin_val, (- pw/2 + radius - 4, y), align = 'right')

    fill(.5)
    oval(-dot_s/2, -dot_s/2, dot_s, dot_s)
    oval(x-dot_s/2, y-dot_s/2, dot_s, dot_s)

saveImage('sine.gif')