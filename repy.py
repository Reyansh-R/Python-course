import pygame
import sys

pygame.init()

window_size = (500, 500)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption(" D: :D 500x500")

image = pygame.image.load("Screenshot 2025-01-27 214733.png")
image = pygame.transform.scale(image, (300, 300))

image_rect = image.get_rect(center=(250, 250))  

font = pygame.font.SysFont("Arial", 32, bold=True)

text = font.render("Teal triangle :3", True, (255, 255, 255))
text_rect = text.get_rect(center=(250, 50)) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

    screen.fill((255, 255, 255))

    
    pygame.draw.rect(screen, (0, 128, 128), (100, 400, 300, 50))

    
    screen.blit(image, image_rect)

    
    screen.blit(text, text_rect)

    
    pygame.display.flip()


pygame.quit()
sys.exit()