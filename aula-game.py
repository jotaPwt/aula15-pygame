import pygame


pygame.init()


size = 500, 500
tela = pygame.display.set_mode(size)
clock = pygame.time.Clock()


pygame.display.set_caption('Joguin')




running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit    :
        
            running = False
        
    tela.fill('#009440')
    
    pygame.draw.rect(tela, 'yellow', [50, 150, 400, 200], 0)
    pygame.draw.circle(tela, (0,10, 220), (250, 250), 50)

    pygame.draw.rect(tela, 'white', [200, 240, 100, 18], 0)

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()

