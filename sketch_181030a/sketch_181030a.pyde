x=0
def setup():
    global holween_good
    size(640, 480)
    holween_good = loadImage("holween_good.png")
    
def draw():
        global x
        background(25,25,112)
        x += 3
        global x
        if x >= 800:
           x = 0
        noStroke()
        fill(255,223,0)
        ellipse(x, height/4.5, 100, 100)
        image(holween_good, 500, 400, 200, 200)
        noStroke()
        fill(255,255,255)
        ellipse(x-20, height/6, 25, 25)
        fill(169,169,169)
        rect(100, 280, 100, 800)
        fill(225, 255, 255)
        rect(120, 400, 50, 50)
        fill(255, 255, 255)
        rect(120, 315, 50, 50)
        fill(169,169,169)
        rect(345, 390, 30, 350)
        fill(255,223,0)
        ellipse(345, 410, 45 ,45)
        ellipse(380, 410, 45 ,45)
        ellipse(360, 380, 45 ,45)
