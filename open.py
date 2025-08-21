import pygame
import sys


pygame.init()


window_size = (500, 500)
screen = pygame.display.set_mode(window_size)


pygame.display.set_caption("pygame Screen :D")


image = pygame.image.load("Screenshot 2025-01-27 214733.png")
image = pygame.transform.scale(image, (300, 300))


image_rect = image.get_rect(center=(250, 250))  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

    
    screen.fill((58, 58, 58))

    
    screen.blit(image, image_rect)

    
    pygame.display.flip()


pygame.quit()
sys.exit()
