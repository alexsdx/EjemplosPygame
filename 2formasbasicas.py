import pygame
pygame.init()
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
rojo = (255, 0, 0)
azul = (0, 0, 255)
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    ventana.fill(blanco)
    pygame.draw.line(ventana, rojo, (100, 100), (700, 500), 5)
    pygame.draw.rect(ventana, azul, (100, 200, 50, 150))
    pygame.draw.circle(ventana, rojo, (400, 200), 30)
    pygame.display.flip()
pygame.quit()