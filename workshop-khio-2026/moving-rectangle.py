
# define and set variables for the frame amount (frame_amount), framewidth (FW) and frame height (FH), and the rectangle width (rect_width)

frame_amount = 60

FW = 920
FH = 440

rect_width = 20

# iterate through the amount of frames and make a new page (which will then be a frame in the animaion)
for frame in range(frame_amount):
    
    newPage(FW, FH)
    # calculate the x position of the rectangle and assign the value to the variable 'x_pos'
    # the value is calculated by dividing the number of the current frame ('frame') by the amount of all frames (frame_amount).
    # this will give any value between 0 and 1 (0/60, 1/60, 2/60, ..., 58/60, 59/60). to get the value of 1 for the last frame we need to divide by (frame_amount - 1). the value of this division is multiplied with the frame width. so it maps the x position to the width of the frame depending on how many frames there are. 
    x_pos = frame / (frame_amount-1) * FW
    # to center the rectangle we subtract half of the width of the rectangle 
    rect(x_pos - rect_width/2, 0, rect_width, height())

# uncomment the next line to save the animation as an gif     
# saveImage('moving-rectangle.gif')

