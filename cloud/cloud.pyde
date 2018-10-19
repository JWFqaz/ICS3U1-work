x=0
def setup():
    background(640, 460)

def draw():
    global x
    if x==640:
        x=0
    x+=5
    background(0)
    print(x)
    ellipse(x, height/2, 50, 50)
