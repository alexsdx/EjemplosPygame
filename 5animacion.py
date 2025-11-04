import pygame
pygame.init()
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
rojo = (255, 0, 0)
x, y = 400, 300
velocidad_x = 5
reloj = pygame.time.Clock()
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    x += velocidad_x
    print(x)
    if x > 750 or x < 50:
        velocidad_x = -velocidad_x
    ventana.fill(blanco)
    pygame.draw.circle(ventana, rojo, (x, y), 30)
    pygame.display.flip()
    reloj.tick(60)  # 60 FPS
pygame.quit()