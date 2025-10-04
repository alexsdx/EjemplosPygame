import pygame
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Control: {joystick.get_name()}")
print(f"Num ejes: {joystick.get_numaxes()}")
print(f"Num botones: {joystick.get_numbuttons()}")
ultimos_ejes = [0.0] * joystick.get_numaxes()
ultimos_botones = [0] * joystick.get_numbuttons()
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
    # Verificar ejes
    for i in range(joystick.get_numaxes()):
        valor_actual = joystick.get_axis(i)
        if abs(valor_actual - ultimos_ejes[i]) > 0.05:  # Umbral para evitar ruido
            print(f"Eje {i}: {valor_actual}")
            ultimos_ejes[i] = valor_actual
    # Verificar botones
    for i in range(joystick.get_numbuttons()):
        valor_actual = joystick.get_button(i)
        if valor_actual != ultimos_botones[i]:
            if valor_actual:
                print(f"Botón {i} presionado")
            else:
                print(f"Botón {i} liberado")
            ultimos_botones[i] = valor_actual
    pygame.time.delay(100)
pygame.joystick.quit()
pygame.quit()