import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Ventana")

# Definir el color (RGB)

blanco = (255, 255, 255)
rojo = (255, 0, 0)
azul = (0, 0, 255)
negro = (0, 0, 0)

COLOR_FONDO = azul

corriendo = True

reloj = pygame.time.Clock()

cont = 0

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
         # Detectar tecla ESC
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
    
    # Llenar la ventana con el color
    ventana.fill(COLOR_FONDO)
    
    # Actualizar la pantalla
    pygame.display.flip()

    print("Frame: ", cont)
    cont = cont + 1

    reloj.tick(60)  # 60 FPS
pygame.quit()