# 12 dots illusion by jacques ninio

# --------
# settings 

pw = 900
cell_s = pw/13
ph = cell_s * 9
strokeW = 8
dot_f = 1.8
dot_s = strokeW * dot_f


# --------
# drawings 
newPage(pw, ph)
fill(None)
stroke(.45)
strokeWidth(strokeW)

# the grid
for i in range(13):
    line((cell_s*i + cell_s/2, 0), (cell_s*i + cell_s/2, ph))
    line((0, cell_s*i + cell_s/2), (pw, cell_s*i + cell_s/2))

for i in range(-9, 13 + 9):
    off = -9 if i % 2 else 9
    line((cell_s*i, 0), (cell_s*(i + off), cell_s*9))

# the dots
stroke(1)
strokeWidth(1)
fill(0)

for i in range(0, 13, 4):
    for j in range(0, 9, 4):
        oval(cell_s*i + cell_s/2 -dot_s/2, cell_s*j + cell_s/2 -dot_s/2, dot_s, dot_s) 


# saveImage('imgs/12dots_grid_illusion.png')