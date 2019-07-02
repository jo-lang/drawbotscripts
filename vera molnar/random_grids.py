import random
# ----------------------
#  settings 

pw = ph = 500
cell_a = 10 # amount of cells
sbdvs = 3 # subdivisions


gap = pw /(cell_a * sbdvs + cell_a + 1)
cell_s = sbdvs * gap

points = [(x * gap, y * gap) for x in range(sbdvs+1) for y in range(sbdvs+1) ] 

# ----------------------
#  function(s)

def a_grid_cell(pos, s, points, amount = len(points)):

    random.shuffle(points)
    points = random.sample( points, amount )

    with savedState():
        translate(x * (cell_s + gap), y * (cell_s + gap))
        polygon(*points, close=False)

# ----------------------
#  drawing

newPage(pw, ph)
rect(0, 0, pw, ph)
translate(gap, gap)

fill(None)
strokeWidth(1)
stroke(1)
lineCap('round')
lineJoin('round')


for x in range( cell_a ):
    for y in range( cell_a ):
        a_grid_cell((x * cell_s, y * cell_s), cell_s, points, y + 3)

# saveImage('random_grids.jpg')