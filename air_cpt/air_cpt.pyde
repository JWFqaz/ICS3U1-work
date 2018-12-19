

'''ball_1_pos_x = 0
ball_1_pos_y = 0
ball_1_speed_x = 0
ball_1_speed_y = 3
ball_1_size = 40

'''ball_2_pos_x = 1
ball_2_pos_y = 1
ball_2_speed_x = 2
ball_2_speed_y = 4
ball_2_size = 40'''

player_pos_x = 0
player_pos_y = 0
player_size = 40
player_img = loadImage("air.png")
background_color = color(39, 76, 119)
player_size= 40
primary_color = color(96, 150, 186)
secondary_color = color(163, 206, 241)

score = 0

def setup():
    size(400, 600)
    
def draw():
    global ball_1_pos_x
    global ball_1_pos_y
    global ball_1_speed_x
    global ball_1_speed_y
    global score
    global player_img
    # Update ball 1's location
    ball_1_pos_y += ball_1_speed_y
    
    # Update player position based on mouse
    player_pos_x = mouseX
    player_pos_y = height - player_size/2
    
    if ball_1_pos_y > height:
        ball_1_pos_y = 0
        ball_1_pos_x = random(0, width)
        score += 1
    
    # Collision detection.
    # Using pythagorean theroem
    radius_ball_1 = ball_1_size/2
    radius_player = player_size/2
    a = ball_1_pos_x - player_pos_x
    b = ball_1_pos_y - player_pos_y
    distance = sqrt(a**2 + b**2)  # hypotenuse of the R-A triangle
    if distance <= radius_ball_1 + radius_player:
        score -= 1
        ball_1_pos_y = 0
        ball_1_pos_x = random(0, width)
        
    '''radius_ball_2 = ball_2_size/2
    radius_player2 = player_size/2
    a = ball_2_pos_x - player_pos_x
    b = ball_2_pos_y - player_pos_y
    distance = sqrt(a**2 + b**2)  # hypotenuse of the R-A triangle
    if distance <= radius_ball_2 + radius_player2:
        score -= 1
        ball_2_pos_y = 0
        ball_2_pos_x = random(0, width)
    background(background_color)  # Remove streaking'''
    
    #Draw ball 1
    noStroke()
    fill(secondary_color)
    ellipse(ball_1_pos_x, ball_1_pos_y, ball_1_size, ball_1_size)
    
    # Draw score
    fill(primary_color)
    textSize(40)
    textAlign(LEFT)
    text(score, 20, 50)'''
    
    
    player_img = loadImage("air.png")
    image(player_img, 20, 45, 78, 56)
