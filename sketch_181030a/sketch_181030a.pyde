x=0
def setup():
    global holween
    size(640, 480)
    holween = loadImage("holween.jpg")
   
def draw():
        background(25,25,112)
    global x
    if x >= 640:
        x = 0
    x += 3
    noStroke()
    fill(255,223,0)
    ellipse(x, height/4.5, 100, 100)
    background(25,25,112)
    image(holween, 50, 50, 550, 550)
    
