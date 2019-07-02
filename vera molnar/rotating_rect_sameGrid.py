# ---------------
#  settings

ph = 500
amount = 24

cell_s = ph / (amount + 2)
pw = 4 * ph - 3 * cell_s
rect_sizes = [ cell_s / 2, cell_s / sqrt(2), 2 * cell_s / ( 1 + sqrt(2) ), cell_s]

grid = [[True if random() > .5 else False for x in range(amount)] for y in range(amount)]


# ---------------
#  drawings

newPage(pw, ph)
translate( cell_s, cell_s)

for rect_s in rect_sizes:
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            with savedState():
                translate( c * cell_s + cell_s/2, r * cell_s + cell_s/2 )
                if cell: rotate(45)
                rect(-rect_s/2, -rect_s/2, rect_s, rect_s)
    translate(ph - cell_s, 0)


# saveImage('rotating_rects_sameGrid.jpg')