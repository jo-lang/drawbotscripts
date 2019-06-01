
w = h = 600
s = 40
off = s/4
shift = 3

x = y = 0

newPage(w, h)
strokeWidth(2)
stroke(.5)

while (y * s) < h:
    while (x *s) < w:

        fill(0) if x % 2 == 0 else fill(1)
        rect(off + x * s, y * s, s, s)
        x += 1

    if y % 3 == 0: off *= -1

    off += s/4
    x = 0
    y += 1

saveImage('imgs/cafe_wall.png')