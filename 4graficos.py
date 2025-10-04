import pygame

pygame.init()

# Dimensiones de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Colores
blanco = (255, 255, 255)
azul = (0, 0, 255)

# Rectángulo
RECT_W, RECT_H = 50, 50
x, y = 400, 300
velocidad = 1

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Evitar que el rectángulo salga de la ventana (clamping)
    if x < 0:
        x = 0
    if x > ANCHO - RECT_W:
        x = ANCHO - RECT_W
    if y < 0:
        y = 0
    if y > ALTO - RECT_H:
        y = ALTO - RECT_H

    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, (x, y, RECT_W, RECT_H))
    pygame.display.flip()

pygame.quit()