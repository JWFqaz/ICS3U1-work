x = 0
def setup():
    size(640, 480)
def draw():
    global x
    
    if x >= 640:
        x = 0
    x += 3
    
    background(135, 206, 250)
    
    noStroke()
    fill(255,255,255)
    ellipse(x, height/3, 50, 50)
    ellipse(x+30, height/3, 50, 50)
    ellipse(x+10, height/3-20, 50, 50)
    fill(139,69,19)
    rect(100, 380, 150, 100)
    fill(255,223,0)
    triangle(100, 380, 190, 300, 250, 380)
    rect(120, 400, 50, 50)
    fill(139,69,19)
    rect(345, 390, 30, 350)
    fill(0, 255, 0)
    ellipse(345, 410, 70 ,70)
    ellipse(380, 410, 70 ,70)
    ellipse(360, 380, 70 ,70)
