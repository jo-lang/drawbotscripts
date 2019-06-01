# grid illusion 

# settings 

pw = ph = 600
grid_lines = 9
bar_s = 11
cell_s = pw/grid_lines
dot_f = 1.25

# drawings 
newPage(pw, ph)
rect(0, 0, pw, ph)

fill(.5)

# the grid
for i in range(grid_lines):
    rect(cell_s*i + cell_s/2 -bar_s/2, 0, bar_s, ph)
    rect(0, cell_s*i + cell_s/2 -bar_s/2, pw, bar_s)

# the dots
fill(1)

for i in range(grid_lines):
    for j in range(grid_lines):
        oval(cell_s*i + cell_s/2 -bar_s/2 * dot_f, 
        cell_s*j + cell_s/2 -bar_s/2 * dot_f, bar_s * dot_f, bar_s * dot_f)
    

# saveImage('imgs/grid_illusion.png')