# --------------
#  settings 

pw = ph = 500
cell_amount = 8
rect_amount = 12
stoke_w = .75
factor = 0.31

colors = [ (random(), random(), random())  for _ in range(5)]

cell_s = pw / (cell_amount + 2)


# --------------
#  function(s)

def get_off(max_val, factor):
     return random() * factor * max_val * choice([-1, 1])
    

def squares(pos, s, amount, rand_f):
    x, y = pos

    for _ in range(amount):
        with savedState():
            translate(randint(int(-s * factor), int(s * factor)), 
            randint(int(-s * factor), int(s * factor)))
            points = [
                (x - s/2 + get_off(s/2, rand_f), y + s/2 + get_off(s/2, rand_f)),
                (x - s/2 + get_off(s/2, rand_f), y - s/2 + get_off(s/2, rand_f)),
                (x + s/2 + get_off(s/2, rand_f), y - s/2 + get_off(s/2, rand_f)),
                (x + s/2 + get_off(s/2, rand_f), y + s/2 + get_off(s/2, rand_f)),
             ]
            polygon(*points)        
         
# --------------
#  drawings 

newPage(pw, ph)
translate(cell_s * 1.5, cell_s * 1.5)

fill(None)
stroke(0)
strokeWidth(stoke_w)
lineJoin('bevel')
lineCap('square')

blendMode("multiply")


for x in range(cell_amount):
    for y in range(cell_amount):
        stroke(*choice(colors))
        squares((x * cell_s, y * cell_s), cell_s, rect_amount, factor)
        
# saveImage('random_squares.jpg')