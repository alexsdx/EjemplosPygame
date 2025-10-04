import pygame
pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi primera ventana")
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
pygame.quit()