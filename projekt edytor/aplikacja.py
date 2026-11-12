import pygame 
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.set_at((event.pos[0], event.pos[1]), (255, 255, 255))
        elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            screen.set_at((event.pos[0], event.pos[1]), (255, 255, 255))
        elif event.type == pygame.KEYDOWN:
            pygame.image.save(screen, "output.png")
    screen.set_at((100,100), (255, 255, 255))
    pygame.display.update()

pygame.quit()