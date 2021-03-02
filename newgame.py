
# Files - https://github.com/techwithtim/pygame-tutorials/tree/master/Game

#import 
import pygame
import random


# Initialize Pygame
pygame.init()

bulletSound = pygame.mixer.Sound('bullet.mp3')
hitSound = pygame.mixer.Sound('hit.mp3')

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 


class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It is derived from the "Sprite" class in Pygame     
    """
     
    def __init__(self, color, width, height):
        """
        Constructor:
        Pass in the color of the the block
        along with it's X and Y positions
        """
         
        # Call the parent class (Sprite) constuctor
        super().__init__()
         
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
     
     
    def reset_pos(self):
        """
        Reset the postion to the top of the screen, at a radom X location. 
        Called by update() def or the main program loop if there is a collision. 
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
     
    def update(self):
        """
        Update - called from each Frame
        """  
         
        # Move block down one pixel  
        self.rect.y += 1
        
        # if block is too far down, rest to the top of screen
        if self.rect.y > 410:
            self.reset_pos() 
         

class Player(Block):
    """
    The player class derives from Block, but overrides the 'updates'
    functionality with a new movement function that will move the block with the 
    mouse.
    """    
    def update(self):
        # Get the current mouse position. This returns the position as
        # a list of numbers
        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]
        self.rect.y = pos[1]



# Play music
bulletSound.play()


# Set the height and width of screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of the 'sprites'.  Each block in the program
# is added to this list.  The list is managed by a class called 'Group'.
block_list = pygame.sprite.Group()

# This is a lsit of every sprite.  All bocks and the ployer block also.
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
    
# Create a red player
player = Player(RED, 20, 15)      
all_sprites_list.add(player)  
    
# Loop until the user clicks the close button
done = False    
    
# Used to manage how fast the screen updates
clock = pygame.time.Clock()  

# Initialize score to zero
score = 0  

# -------------------   Main Loop for Program ---------------------------

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(WHITE)
    
    # Call update() method on every sprite in the list
    all_sprites_list.update()
    
    # See if the player block has hit anything 
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    
    # Check the list of collisions 
    for block in blocks_hit_list:
        score += 1
        hitSound.play()
        print (score)
        
        # Reset to the top of the screen to fall again.
        block.reset_pos()
        
    # Draw all the sprites
    all_sprites_list.draw(screen)     
    
    # Limit to 20 frames per second
    clock.tick(20)
    
    # Go ahead and update the screen with what has been drawn
    pygame.display.flip()
       
# Quit the game
pygame.quit() 
   