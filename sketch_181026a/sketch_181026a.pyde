def setup():
    global earth_img   
    size(640, 480)
    earth_img=loadImage("data/The_Earth_seen_from_Apollo_17. jpg")
    
def draw():
    background(100, 60, 200)
    image(earth_img, 100, 100)
