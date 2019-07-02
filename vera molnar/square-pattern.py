# --------------
#  settings 

pw = ph = 500
sq_amount = 8
rings = 8
st_w = 1
threshold = .99

cell_s = (pw - st_w) / sq_amount

# --------------
#  function(s) 

def c_rect(pos, s):
    x, y = pos
    rect(x - s/2, y - s/2, s, s)

# --------------
#  drawing

newPage(pw, ph)
rect(0, 0, pw, ph)
translate(st_w/2, st_w/2)
strokeWidth(st_w)

for x in range (sq_amount):
    for y in range (sq_amount):
        fill(None)
        stroke(1)
        for r in range(1, rings+1):
            if random() > threshold and r != rings:
                continue
            c_rect((x * cell_s + cell_s/2, y * cell_s + cell_s/2), cell_s * r/rings)
        fill(1)
        stroke(None)
        if random() > threshold:
            continue
        c_rect((x * cell_s + cell_s/2, y * cell_s + cell_s/2), st_w)
        
# saveImage('square_pattern.jpg')