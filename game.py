import math
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1200, 710))
clock = pygame.time.Clock()
pygame.display.set_caption('Monster Run')

# replace icon image
# pygame.display.set_icon()

# BACKGROUND LOGIC - infinte scroll + moving background (each layer moves at slightly different speed)
# add all layers to array and stack them on screen - one on top of the other in same order
bg_imgs = []
for i in range(1, 13):
    bg_img = pygame.image.load(f'assets/bg/bg_{i}.png').convert_alpha()
    bg_imgs.append(bg_img)
    
bg_width = bg_imgs[0].get_width()
    
# x represents the # of times the image is repeated & we stack it horizontally via (x*bg_width)
def generate_bg():
    for x in range(0, bg_tiles):
        speed = 1
        for i in bg_imgs:
            screen.blit(i, ((x*bg_width) - scroll * speed,-83)) #adjusted y-axis to make image fit nicely
            speed += 0.2
            
# GAME VARIABLES
scroll = 0
bg_tiles = math.ceil(1200 / bg_width) + 3  #the 3 prevents the background from bleeding (1 and 2 weren't enough)

# NEED TO DO:
# text_surface, player_surface, monster_surface

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit('Game closed') #this ends while loop
            
    # key press actions
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        scroll += 5
    # elif key[pygame.K_RIGHT]:
    #     scroll += 5
    
    # drawing the background
    generate_bg()
    
    # reset bg when scrolling to keep bg quality
    if scroll > bg_width:
        scroll = 0

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60