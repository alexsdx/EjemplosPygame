import pygame

# Inicializar Pygame y el módulo de joystick
pygame.init()
pygame.joystick.init()

# Verificar si hay un control conectado
if pygame.joystick.get_count() == 0:
    print("No se detectó ningún control. Usa las teclas como respaldo.")
    usar_control = False
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Control detectado: {joystick.get_name()}")
    usar_control = True

# Configurar la ventana
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)
x, y = 400, 300  # Posición inicial del rectángulo
velocidad = 5    # Velocidad de movimiento
reloj = pygame.time.Clock()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Obtener entrada del control (si está disponible) o del teclado
    if usar_control:
        # Leer los ejes del joystick (normalmente eje 0 para X, eje 1 para Y)
        eje_x = joystick.get_axis(0)  # Izquierda/Derecha
        eje_y = joystick.get_axis(1)  # Arriba/Abajo
        # Mover solo si el valor del eje supera un umbral (evita deriva)
        if abs(eje_x) > 0.1:
            x += velocidad * eje_x
        if abs(eje_y) > 0.1:
            y += velocidad * eje_y
    else:
        # Respaldo con teclado (como en el código original)
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            x -= velocidad
        if teclas[pygame.K_RIGHT]:
            x += velocidad
        if teclas[pygame.K_UP]:
            y -= velocidad
        if teclas[pygame.K_DOWN]:
            y += velocidad

    # Limitar el rectángulo dentro de la ventana
    x = max(0, min(x, 800 - 50))  # 50 es el ancho del rectángulo
    y = max(0, min(y, 600 - 50))  # 50 es el alto del rectángulo

    # Determinar color: azul por defecto, rojo si se mantiene presionado "botón 1" del control
    color = azul
    if usar_control:
        # joystick.get_button(index) devuelve 1 si está pulsado
        try:
            if joystick.get_button(1):  # botón 1 (índice 1)
                color = rojo
        except pygame.error:
            # Si hay algún problema leyendo el joystick, continuar con el color por defecto
            pass
    else:
        # Soporte alternativo: pulsar la tecla '1' en el teclado hará lo mismo
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_1]:
            color = rojo

    # Dibujar
    ventana.fill(blanco)
    pygame.draw.rect(ventana, color, (x, y, 50, 50))
    pygame.display.flip()
    reloj.tick(60)  # 60 FPS

# Finalizar
pygame.joystick.quit()
pygame.quit()