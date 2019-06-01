
grid = 12
page_s = 600
frames = 48

tile_s = page_s/grid

rhythm = [1, 0, 0, 1, 0, 1, 1, 0]

def cross(pos, s):
    x, y = pos
    polygon((x - s/2, y),
            (x - s/2 + s/8, y - s/8),
            (x - s/8, y - s/8),
            (x - s/8, y - s/2 + s/8),
            (x, y - s/2),
            (x + s/8, y - s/2 + s/8),
            (x + s/8, y - s/8),
            (x + s/2 - s/8, y - s/8),
            (x + s/2, y),
            (x + s/2 - s/8, y + s/8),
            (x + s/8, y + s/8),
            (x + s/8, y + s/2 - s/8),
            (x, y + s/2),
            (x - s/8, y + s/2 - s/8),
            (x - s/8, y + s/8),
            (x - s/2 + s/8, y + s/8)
        )

for f in range(frames):

    newPage(page_s, page_s)
    frameDuration(.1)
    # linear 
    alpha = f / frames if f < (frames) else 2 - (f / frames)
    # sinus wave 
    alpha = .5 + .5 * sin(f/frames * 2 * pi)

    for y in range(grid):
        for x in range(grid):

            fill(.8) if (x+y) % 2 == 0 else fill(.7)
            rect(x * tile_s, y * tile_s, tile_s, tile_s)
            shift = (x + y) % len(rhythm)
            fill(1, alpha) if rhythm[ shift ] else fill(.5, alpha)
            cross((x * tile_s, y * tile_s), tile_s/3 )
            
# saveImage('wavy_checkerboard.gif')
