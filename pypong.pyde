# PONG programmed in processing python by Kyle Johnson

screen_width = 640
screen_height = 480

class player:
    def __init__(self, x_pos, y_pos, p_width, p_height):
        self.x = x_pos
        self.y = y_pos
        self.width = p_width
        self.height = p_height
        self.score = 0
        self.direction = 0
    
    def draw(self):
        rect(self.x, self.y, self.width, self.height)
        textSize(32)
        text(str(self.score), self.x + 40, 32)
        text(str(self.score), self.x - 40, 32)
        
class ball:
    def __init__(self, x_pos, y_pos, radius, velocity, direction):
        self.x = x_pos
        self.y = y_pos
        self.radius = radius
        self.velocity = velocity*direction
        self.yvelocity = 0
        self.direction = direction
        
    def reset(self):
        self.direction = -self.direction
        self.x = screen_width/2
        self.y = screen_height/2
        self.radius = self.radius
        self.velocity = 100*self.direction
    
    def draw(self):
        ellipseMode(CENTER)
        ellipse(self.x, self.y, 2*self.radius, 2*self.radius)
        
    def update(self):
        self.x = self.x + (self.velocity)/frameRate
        self.y = self.y + self.yvelocity/frameRate
    
    def collide(self, left_player, right_player):
        destroyed = False
        
        # Travelling to the left
        if (self.velocity < 0):
            # Touching the left panel
            if ((self.x - self.radius) <= (left_player.x + left_player.width) and self.y >= left_player.y and self.y <= left_player.y + left_player.height):
                self.velocity = -self.velocity
                self.yvelocity = left_player.direction * abs(self.velocity)
            
            # Passing the left border of the game
            if ((self.x - self.radius) <= 0):
                right.score += 1
                destroyed = True
            
        # Travelling to the right
        if (self.velocity > 0):
            # Touching the right panel
            if ((self.x + self.radius) >= (right_player.x) and self.y >= right_player.y and self.y <= right_player.y + right_player.height):
                self.velocity = -self.velocity
                self.yvelocity = right_player.direction * abs(self.velocity)
            
            # Passing the right border of the game
            if ((self.x + self.radius) >= screen_width):
                left.score += 1
                destroyed = True
            
        # Touching either the upper or lower boundary of the game
        if (self.y >= screen_height or self.y <= 0):
            self.yvelocity = -self.yvelocity
            
        return destroyed
        
left = player(10, 200, 20, 250)
right = player(screen_width - 10 - 20, 200, 20, 250)
ping = ball(screen_width/2, screen_height/2, 10, 125, -1)


def setup():
    size(screen_width, screen_height)
    
def draw():
    # Drawing routine
    background(167)
    left.draw()
    right.draw()
    ping.draw()
    
    if left.score >= 10:
        text("Left PLAYER wins!", screen_width/2, screen_height/2, 32)
    
    if right.score >= 10:
        text("right PLAYER wins!", screen_width/2, screen_height/2, 32)
    
    # Interactions routine
    #Keypresses are handled here
    if (ping.collide(left, right)):
        ping.reset()
    else:
        ping.update()
    
def keyPressed():
    if (key == 'w'):
        left.y -= 5
        left.direction = -1
    if (key == 's'):
        left.y += 5
        left.direction = 1

    if (key == 'i'):
        right.y -= 5
        right.direction = -1
    if (key == 'k'):
        right.y += 5
        right.direction = 1
        
    if (key == 's' and key == 'w'):
        left.direction = 0
    if (key == 'k' and key == 'i'):
        right.direction = 0
