import pygame

pygame.init()

p = pygame.display.set_mode((600,900))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()