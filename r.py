import pygame
pygame.init()
screen = pygame.display.set_mode((450,680))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.draw.rect(screen, (125,210,50), pygame.Rect(30,30,60,60))
        pygame.draw.circle(screen, (9,255,255), (300,300), 50)
        pygame.draw.circle(screen, (255,0,255),(100,150), 50, 3)
    pygame.display.flip()
    
    
    


