import asyncio
import platform
import pygame
import random

# Configuración inicial
ANCHO = 800
ALTO = 600
FPS = 60
TAMANO_JUGADOR = (50, 30)
TAMANO_INVASOR = (40, 30)
TAMANO_DISPARO = (5, 10)
VELOCIDAD_JUGADOR = 5
VELOCIDAD_INVASOR = 1
VELOCIDAD_DISPARO = 7

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

class SpaceInvaders:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Space Invaders")
        self.reloj = pygame.time.Clock()
        
        # Jugador
        self.jugador = pygame.Rect(ANCHO // 2 - TAMANO_JUGADOR[0] // 2, ALTO - 50, *TAMANO_JUGADOR)
        self.disparos = []  # Lista de disparos del jugador
        
        # Invasores
        self.invasores = []
        self.crear_invasores()
        
        # Variables del juego
        self.puntuacion = 0
        self.vidas = 3
        self.fuente = pygame.font.SysFont("arial", 24)
        self.game_over = False
        self.direccion_invasores = 1  # 1: derecha, -1: izquierda
    
    def crear_invasores(self):
        # Crear una formación de invasores (5 filas x 11 columnas)
        for fila in range(5):
            for columna in range(11):
                x = 50 + columna * 60
                y = 50 + fila * 50
                self.invasores.append(pygame.Rect(x, y, *TAMANO_INVASOR))
    
    def setup(self):
        self.pantalla.fill(NEGRO)  # Fondo negro
    
    def update_loop(self):
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not self.game_over:
                    # Disparar
                    disparo = pygame.Rect(self.jugador.centerx - TAMANO_DISPARO[0] // 2, 
                                          self.jugador.top, *TAMANO_DISPARO)
                    self.disparos.append(disparo)
                elif evento.key == pygame.K_r and self.game_over:
                    # Reiniciar juego
                    self.invasores.clear()
                    self.crear_invasores()
                    self.disparos.clear()
                    self.jugador.centerx = ANCHO // 2
                    self.puntuacion = 0
                    self.vidas = 3
                    self.game_over = False
        
        if not self.game_over:
            # Movimiento del jugador
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] and self.jugador.left > 0:
                self.jugador.x -= VELOCIDAD_JUGADOR
            if teclas[pygame.K_RIGHT] and self.jugador.right < ANCHO:
                self.jugador.x += VELOCIDAD_JUGADOR
            
            # Movimiento de disparos
            for disparo in self.disparos[:]:
                disparo.y -= VELOCIDAD_DISPARO
                if disparo.bottom < 0:
                    self.disparos.remove(disparo)
            
            # Movimiento de invasores
            mover_abajo = False
            for invasor in self.invasores:
                invasor.x += VELOCIDAD_INVASOR * self.direccion_invasores
                # Verificar si tocan los bordes laterales
                if invasor.right >= ANCHO or invasor.left <= 0:
                    mover_abajo = True
            
            if mover_abajo:
                self.direccion_invasores *= -1  # Cambiar dirección
                for invasor in self.invasores:
                    invasor.y += TAMANO_INVASOR[1]  # Bajar un nivel
            
            # Colisiones: disparos con invasores
            for disparo in self.disparos[:]:
                for invasor in self.invasores[:]:
                    if disparo.colliderect(invasor):
                        self.disparos.remove(disparo)
                        self.invasores.remove(invasor)
                        self.puntuacion += 10
                        break
            
            # Verificar Game Over
            for invasor in self.invasores:
                if invasor.bottom >= ALTO or invasor.colliderect(self.jugador):
                    self.vidas -= 1
                    if self.vidas <= 0:
                        self.game_over = True
                    else:
                        # Reiniciar posiciones si pierde una vida
                        self.invasores.clear()
                        self.crear_invasores()
                        self.disparos.clear()
                    break
            
            # Ganar nivel (si eliminan todos los invasores)
            if not self.invasores:
                self.crear_invasores()
        
        # Dibujar elementos
        self.pantalla.fill(NEGRO)
        
        # Dibujar jugador
        pygame.draw.rect(self.pantalla, AZUL, self.jugador)
        
        # Dibujar invasores
        for invasor in self.invasores:
            pygame.draw.rect(self.pantalla, ROJO, invasor)
        
        # Dibujar disparos
        for disparo in self.disparos:
            pygame.draw.rect(self.pantalla, BLANCO, disparo)
        
        # Dibujar puntuación y vidas
        texto_puntuacion = self.fuente.render(f"Puntuación: {self.puntuacion}", True, BLANCO)
        texto_vidas = self.fuente.render(f"Vidas: {self.vidas}", True, BLANCO)
        self.pantalla.blit(texto_puntuacion, (10, 10))
        self.pantalla.blit(texto_vidas, (ANCHO - 100, 10))
        
        # Mostrar Game Over
        if self.game_over:
            texto_game_over = self.fuente.render("Game Over! Presiona R para reiniciar", True, BLANCO)
            self.pantalla.blit(texto_game_over, (ANCHO // 2 - 200, ALTO // 2))
        
        pygame.display.flip()
        self.reloj.tick(FPS)
        return True

async def main():
    juego = SpaceInvaders()
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