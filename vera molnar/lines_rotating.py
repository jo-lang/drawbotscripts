# --------------
#  settings 

pw = ph = 500
amount = 24
st_w = 4

cell_s = pw / (amount + 2)
line_cap = (st_w/2)/sqrt(2)

possible_vectors = [ 
    [(-1, -1), (1,  1)],
    [(-1,  1), (1, -1)],
    [( 0,  1), (0, -1)],
    [(-1,  0), (1,  0)] ]

# --------------
#  function(s)

def rnd(x, val): return round(x, val)

def rnd_p(p, val=3): return rnd(p[0], val), rnd(p[1], val)
    
def a_line(pos, s):
    global visited
    x, y = pos
    selected = choice(possible_vectors)

    p1_, p2_ = [rnd_p((x + x_off * s/2, y + y_off * s/2)) for x_off, y_off in selected]
    p1, p2 = p1_, p2_
    
    if p1_ in visited and 0 not in selected[0]:
        p1 = p1[0] + selected[0][0]*line_cap, p1[1] + selected[0][1]*line_cap
    if p2_ in visited and 0 not in selected[1]:
        p2 = p2[0] + selected[1][0]*line_cap, p2[1] + selected[1][1]*line_cap

    line(p1, p2)
    stroke(0)
    for p in [p1_, p2_]: 
        visited[p] = visited.get(p, True)

# --------------
#  drawings 

newPage(pw, ph)
translate(cell_s * 1.5, cell_s * 1.5)

fill(None)
stroke(0)
strokeWidth(st_w)

visited = {}

for x in range(amount):
    for y in range(amount):
        a_line((x * cell_s, y * cell_s), cell_s)
        
# saveImage('lines_rotating.jpg')