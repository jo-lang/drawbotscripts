w, h = 600, 600

newPage(w, h)

fill(1, 1, 0.7)
rect(0, 0, w, h)

fill(0)

polygon((w,h/3*2), (w,h), (w/3, h), (w/9*7, h/3*2))
polygon((w,h/3), (w,0), (w/3, 0), (w/9*7, h/3))

fill(None)
strokeWidth(3)
lineCap('round')
stroke(0)

line((0, h/3*2), (w/3, h/3*2))
line((w/3, h/3*2), (w/3, h))

line((0, h/3), (w/3, h/3))
line((w/3, h/3), (w/3, 0))

line((w/9*7, h/9*4), (w, h/9*4))
line((w/9*7, h/9*5), (w, h/9*5))

line((w/3, h/3), (w/9*7, h/9*4))
line((w/3, h/3*2), (w/9*7, h/9*5))


stroke(1, 0, 0)

line((w/3, h/3), (w/3, h/3*2))
line((w/9*7, h/3), (w/9*7, h/3*2))

# saveImage('perspective.png')