x=0
def setup():
    global holween_good
    global download
    global spider
    size(640, 480)
    holween_good = loadImage("holween_good.png")
    download = loadImage("download.png")
    spider = loadImage ("800px_COLOURBOX2275255.jpg")
def draw():
        global x
        background(0, 0, 0)
        x += 3
        global x
        if x >= 640:
           x = 0
        noStroke()
        fill(255,223,0)
        ellipse(x-10, height/7, 100, 100)
        image(holween_good, 500, 400, 200, 200)
        image (download, 400, 200, 100, 100)
        image( spider, -10, 150, 115, 115)
        fill(255,255,255)
        ellipse(x-30, height/7, 25, 25)
        fill(169,169,169)
        rect(100, 280, 100, 800)
        fill(225, 255, 255)
        rect(120, 400, 50, 50)
        fill(255, 255, 255)
        rect(120, 315, 50, 50)
        fill(169,169,169)
        rect(345, 390, 30, 350)
        fill(255,223,0)
        ellipse(335, 420, 45 ,45)
        ellipse(390, 420, 45 ,45)
        ellipse(360, 380, 45 ,45)
