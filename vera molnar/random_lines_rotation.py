# -----------------
#  settings 

pw = ph = 500
amount = 36
threshold = .98 # a value between 0 and 1 
st_w = 3

ele_s = pw / (amount + 2)

# -----------------
#  drawing 

newPage(pw, ph)
translate(ele_s*1.5, ele_s*1.5)

fill(None)
stroke(0)
strokeWidth(st_w)
lineCap('round')

for x in range(amount):
    for y in range(amount + 1):
        with savedState():
            translate(x * ele_s, y * ele_s - ele_s/2) 
            if random() > threshold:
                rotate(random() * 180)
            line( (-ele_s/2, 0), (ele_s/2, 0) )
        
# saveImage('random_lines_rotation.jpg')