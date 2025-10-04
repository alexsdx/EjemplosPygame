import asyncio
import platform
import pygame
import random

# Configuración inicial
FPS = 60
ANCHO = 800
ALTO = 600
TAMANO_PADDLE = (20, 100)
TAMANO_PELOTA = 20
VELOCIDAD_PADDLE = 5
VELOCIDAD_PELOTA = 7

class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Pong")
        self.reloj = pygame.time.Clock()
        
        # Paletas y pelota
        self.paddle_jugador = pygame.Rect(50, ALTO // 2 - TAMANO_PADDLE[1] // 2, *TAMANO_PADDLE)
        self.paddle_computadora = pygame.Rect(ANCHO - 50 - TAMANO_PADDLE[0], ALTO // 2 - TAMANO_PADDLE[1] // 2, *TAMANO_PADDLE)
        self.pelota = pygame.Rect(ANCHO // 2 - TAMANO_PELOTA // 2, ALTO // 2 - TAMANO_PELOTA // 2, TAMANO_PELOTA, TAMANO_PELOTA)
        
        # Velocidad inicial de la pelota
        self.velocidad_pelota = [VELOCIDAD_PELOTA * random.choice((1, -1)), VELOCIDAD_PELOTA * random.choice((1, -1))]
        
        # Puntuación
        self.puntuacion_jugador = 0
        self.puntuacion_computadora = 0
        self.fuente = pygame.font.SysFont("arial", 36)
        
    def setup(self):
        self.pantalla.fill((0, 0, 0))  # Fondo negro
        
    def update_loop(self):
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
        
        # Movimiento del jugador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and self.paddle_jugador.top > 0:
            self.paddle_jugador.y -= VELOCIDAD_PADDLE
        if teclas[pygame.K_DOWN] and self.paddle_jugador.bottom < ALTO:
            self.paddle_jugador.y += VELOCIDAD_PADDLE
        
        # Movimiento de la computadora (IA simple)
        if self.paddle_computadora.centery < self.pelota.centery and self.paddle_computadora.bottom < ALTO:
            self.paddle_computadora.y += VELOCIDAD_PADDLE
        if self.paddle_computadora.centery > self.pelota.centery and self.paddle_computadora.top > 0:
            self.paddle_computadora.y -= VELOCIDAD_PADDLE
        
        # Movimiento de la pelota
        self.pelota.x += self.velocidad_pelota[0]
        self.pelota.y += self.velocidad_pelota[1]
        
        # Colisiones con bordes superior e inferior
        if self.pelota.top <= 0 or self.pelota.bottom >= ALTO:
            self.velocidad_pelota[1] = -self.velocidad_pelota[1]
        
        # Colisiones con paletas
        if self.pelota.colliderect(self.paddle_jugador) or self.pelota.colliderect(self.paddle_computadora):
            self.velocidad_pelota[0] = -self.velocidad_pelota[0]
        
        # Puntuación
        if self.pelota.left <= 0:
            self.puntuacion_computadora += 1
            self.resetear_pelota()
        elif self.pelota.right >= ANCHO:
            self.puntuacion_jugador += 1
            self.resetear_pelota()
        
        # Dibujar elementos
        self.pantalla.fill((0, 0, 0))  # Limpiar pantalla
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.paddle_jugador)  # Paleta jugador
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.paddle_computadora)  # Paleta computadora
        pygame.draw.ellipse(self.pantalla, (255, 255, 255), self.pelota)  # Pelota
        pygame.draw.aaline(self.pantalla, (255, 255, 255), (ANCHO // 2, 0), (ANCHO // 2, ALTO))  # Línea central
        
        # Mostrar puntuación
        texto_jugador = self.fuente.render(str(self.puntuacion_jugador), True, (255, 255, 255))
        texto_computadora = self.fuente.render(str(self.puntuacion_computadora), True, (255, 255, 255))
        self.pantalla.blit(texto_jugador, (ANCHO // 4, 20))
        self.pantalla.blit(texto_computadora, (3 * ANCHO // 4, 20))
        
        pygame.display.flip()
        self.reloj.tick(FPS)
        return True
    
    def resetear_pelota(self):
        self.pelota.center = (ANCHO // 2, ALTO // 2)
        self.velocidad_pelota = [VELOCIDAD_PELOTA * random.choice((1, -1)), VELOCIDAD_PELOTA * random.choice((1, -1))]

async def main():
    juego = Pong()
    juego.setup()
    while True:
        if not juego.update_loop():
            break
        await asyncio.sleep(1.0 / FPS)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())