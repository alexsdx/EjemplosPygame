import pygame
pygame.init()
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)
# Fuente para mostrar texto en pantalla
font = pygame.font.Font(None, 36)
jugador = pygame.Rect(400, 300, 50, 50)
objetivo = pygame.Rect(200, 200, 30, 30)
# Velocidad en píxeles por segundo (ajusta este valor para cambiar qué tan rápido se mueve)
velocidad = 300
# Reloj para controlar FPS y obtener delta time
clock = pygame.time.Clock()

# Posición en float para movimiento suave independiente de FPS
player_x = float(jugador.x)
player_y = float(jugador.y)
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    teclas = pygame.key.get_pressed()
    # dt en segundos (tiempo desde el último frame)
    dt = clock.tick(60) / 1000.0  # limita a 60 FPS y devuelve ms

    # Mover usando velocidad (píxeles/segundo) * dt (segundos)
    if teclas[pygame.K_LEFT]:
        player_x -= velocidad * dt
    if teclas[pygame.K_RIGHT]:
        player_x += velocidad * dt
    if teclas[pygame.K_UP]:
        player_y -= velocidad * dt
    if teclas[pygame.K_DOWN]:
        player_y += velocidad * dt
    # Limitar jugador dentro de los bordes de la ventana
    # Limitar dentro de la ventana (aplicar sobre las posiciones float)
    if player_x < 0:
        player_x = 0
    if player_x > 800 - jugador.width:
        player_x = 800 - jugador.width
    if player_y < 0:
        player_y = 0
    if player_y > 600 - jugador.height:
        player_y = 600 - jugador.height

    # Sincronizar rect con la posición
    jugador.x = int(player_x)
    jugador.y = int(player_y)
    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, jugador)
    pygame.draw.rect(ventana, rojo, objetivo)
    # Mostrar texto en pantalla cuando hay colisión
    if jugador.colliderect(objetivo):
        texto = font.render("¡Colisión!", True, (0, 0, 0))
        rect_texto = texto.get_rect(center=(ventana.get_width() // 2, 30))
        ventana.blit(texto, rect_texto)
    pygame.display.flip()
pygame.quit()