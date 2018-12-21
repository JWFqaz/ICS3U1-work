def setup():
    size(1000, 1000)
    
def draw():
    background(0, 0, 0)
    x_player=mouseX
    y_player= mouseY
    air = loadImage("air.jpg")
    image(air, x_player, y_player, 70, 70)
