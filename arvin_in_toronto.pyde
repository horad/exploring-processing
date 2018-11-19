arvin_pos_x = 0
arvin_pos_y = 0
arvin_speed_y = 11
arvin_speed_x = 11 


def setup():
    global arvin
    global back_img
    x = 0

    size(1000,750)
    arvin = loadImage("Bart_Simpson.png")
    back_img = loadImage("travel_log_hanlans_201807161.jpg")

#arvinpicture
def draw():
    global arvin_pos_x, arvin_pos_y, arvin_speed_x, arvin_speed_y
    background(back_img)
    image(arvin, arvin_pos_x, arvin_pos_y, width/4, height/4)
    
    arvin_pos_x += arvin_speed_x
    arvin_pos_y += arvin_speed_y
    if arvin_pos_x < 0 or arvin_pos_x > width*3/4:
        arvin_speed_x *= -1
    elif arvin_pos_y < 0 or arvin_pos_y > height*3/4:
        arvin_speed_y *= -1
    
    textSize(25)
    fill(255, 255, 255)
    text("arvin in toronto", 45, 100)
    
    ellipseMode(CENTER)
    fill(252, 0, 0)
    quad(38, 31, 86, 20, 69, 63, 30, 76)  
