
pw = ph = 500 # width and height of the canvas 
granularity = 20 # amount of columns and rows 

max_dia = pw / granularity

newPage(pw, ph)
translate(max_dia/2, max_dia/2)

for x in range(granularity):
    for y in range(granularity):
        r  = random()
        dia = max_dia * r
        fill(r)
        oval(x * max_dia - dia/2, y * max_dia - dia/2, dia, dia)
        
# saveImage('dots_size_vs_darkness.jpg')