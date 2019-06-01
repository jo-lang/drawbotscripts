page_s = 500
cell_amount = 12

rhythm = [1, 0, 0, 1, 0, 1, 1, 0]

cell_s = page_s / cell_amount
corner_s = cell_s/4

newPage(page_s, page_s)
translate(-cell_s/2, -cell_s/2)

def lozenge(pos, s):
    x, y = pos
    polygon((x, y), (x + s/2, y + s/2), (x + s, y), (x + s/2, y - s/2))

for x in range(cell_amount+1):
    for y in range(cell_amount+1):
        pos_x, pos_y = x * cell_s, y * cell_s
        fill(0.5) if (x+y) % 2 == 0 else fill(1)
        rect(pos_x, pos_y, cell_s, cell_s)

        fill(1)
        lozenge((pos_x - corner_s, pos_y), corner_s*2)

        fill(0)
        shift = (x + y) % len(rhythm)

        if rhythm[ shift ]:
            lozenge((pos_x - corner_s, pos_y), corner_s)
            lozenge((pos_x, pos_y), corner_s)
        else:
            lozenge((pos_x - corner_s/2, pos_y + corner_s/2), corner_s)
            lozenge((pos_x - corner_s/2, pos_y - corner_s/2), corner_s)
            
# saveImage('rotating_checkerboard.png')