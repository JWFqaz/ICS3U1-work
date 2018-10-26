slide=0

def setup():
    size(640, 480)

def draw():
    global slide
    if frameCount % 60*2==0:
        slide+=1
        if slide>=4:
            slide=0
    elif slide == 1:
        background(60, 255, 70)
    elif slide == 2:
        background(40, 189, 20)
    elif slide == 3:
        background(255, 98, 24)
    def mousePressed():
        global slide
        slide+=1
        if slide>=4:
            slide=0
