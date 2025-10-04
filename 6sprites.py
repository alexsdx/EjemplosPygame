import pygame
import math

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)

# Cargar y redimensionar la imagen
imagen_original = pygame.image.load("logo-itcm-v2.png")  # Asegúrate de tener la imagen
# Redimensionar a 100x100 píxeles (ajusta según necesites)
imagen = pygame.transform.scale(imagen_original, (500, 500))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Obtener posición del ratón y calcular ángulo
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angulo = math.atan2(mouse_y - 300, mouse_x - 400) * 180 / math.pi

    # Rotar la imagen redimensionada
    imagen_rotada = pygame.transform.rotate(imagen, -angulo)

    # Dibujar
    ventana.fill(blanco)
    ventana.blit(imagen_rotada, (400 - imagen_rotada.get_width() // 2, 300 - imagen_rotada.get_height() // 2))
    pygame.display.flip()

pygame.quit()