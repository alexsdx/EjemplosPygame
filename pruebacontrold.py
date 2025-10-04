import pygame
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Control: {joystick.get_name()}")
print(f"Num ejes: {joystick.get_numaxes()}")
print(f"Num botones: {joystick.get_numbuttons()}")
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    for i in range(joystick.get_numaxes()):
        print(f"Eje {i}: {joystick.get_axis(i)}")
    for i in range(joystick.get_numbuttons()):
        if joystick.get_button(i):
            print(f"Botón {i} presionado")
    pygame.time.delay(100)
pygame.quit()