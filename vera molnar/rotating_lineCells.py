

pw = ph = 500
amount = 27

cell_s = pw / (amount + 1)
line_l = cell_s * .9

newPage(pw, ph)
translate(cell_s/2, cell_s/2)

fill(None)
stroke(0)
strokeWidth(1)

for y in range(amount):
    line_amount = 3 - y // 9
    y_shift = cell_s / line_amount
    for x in range(amount):
        
        with savedState():        
            translate(x * cell_s + cell_s/2, y * cell_s + cell_s/2)
            rotate(random() * 180)
            translate(0, -cell_s/2 + y_shift/2) 
            
            for l in range(line_amount):
                line((-line_l/2, y_shift * l), (line_l/2, y_shift * l))
                
# saveImage('rotating_lineCells.jpg')