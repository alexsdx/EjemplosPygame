import asyncio
import platform
import pygame
import random

# Configuración inicial
ANCHO = 800
ALTO = 600
TAMANO_CELDA = 20
FPS = 15  # Controla la velocidad del juego

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Snake")
        self.reloj = pygame.time.Clock()
        
        # Inicializar serpiente
        self.snake = [(ANCHO // 2, ALTO // 2)]  # Lista de coordenadas (x, y)
        self.direccion = (1, 0)  # Dirección inicial: derecha (dx, dy)
        self.comida = self.generar_comida()
        self.puntuacion = 0
        self.fuente = pygame.font.SysFont("arial", 36)
        self.game_over = False
    
    def generar_comida(self):
        # Generar comida en una posición aleatoria en la cuadrícula
        while True:
            x = random.randrange(0, ANCHO, TAMANO_CELDA)
            y = random.randrange(0, ALTO, TAMANO_CELDA)
            if (x, y) not in self.snake:
                return (x, y)
    
    def setup(self):
        self.pantalla.fill(NEGRO)  # Fondo negro
    
    def update_loop(self):
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            elif evento.type == pygame.KEYDOWN and not self.game_over:
                # Cambiar dirección según la tecla
                if evento.key == pygame.K_UP and self.direccion != (0, 1):
                    self.direccion = (0, -1)
                elif evento.key == pygame.K_DOWN and self.direccion != (0, -1):
                    self.direccion = (0, 1)
                elif evento.key == pygame.K_LEFT and self.direccion != (1, 0):
                    self.direccion = (-1, 0)
                elif evento.key == pygame.K_RIGHT and self.direccion != (-1, 0):
                    self.direccion = (1, 0)
                elif evento.key == pygame.K_r and self.game_over:
                    # Reiniciar juego
                    self.snake = [(ANCHO // 2, ALTO // 2)]
                    self.direccion = (1, 0)
                    self.comida = self.generar_comida()
                    self.puntuacion = 0
                    self.game_over = False
        
        if not self.game_over:
            # Mover la serpiente
            cabeza_x, cabeza_y = self.snake[0]
            nueva_cabeza = (cabeza_x + self.direccion[0] * TAMANO_CELDA, 
                           cabeza_y + self.direccion[1] * TAMANO_CELDA)
            
            # Verificar colisiones
            if (nueva_cabeza in self.snake or 
                nueva_cabeza[0] < 0 or nueva_cabeza[0] >= ANCHO or 
                nueva_cabeza[1] < 0 or nueva_cabeza[1] >= ALTO):
                self.game_over = True
            
            # Actualizar serpiente
            self.snake.insert(0, nueva_cabeza)
            
            # Verificar si comió comida
            if nueva_cabeza == self.comida:
                self.puntuacion += 1
                self.comida = self.generar_comida()
            else:
                self.snake.pop()
        
        # Dibujar elementos
        self.pantalla.fill(NEGRO)
        # Dibujar serpiente
        for segmento in self.snake:
            pygame.draw.rect(self.pantalla, VERDE, 
                            (segmento[0], segmento[1], TAMANO_CELDA, TAMANO_CELDA))
        # Dibujar comida
        pygame.draw.rect(self.pantalla, ROJO, 
                        (self.comida[0], self.comida[1], TAMANO_CELDA, TAMANO_CELDA))
        # Dibujar puntuación
        texto_puntuacion = self.fuente.render(f"Puntuación: {self.puntuacion}", True, BLANCO)
        self.pantalla.blit(texto_puntuacion, (10, 10))
        
        # Mostrar Game Over
        if self.game_over:
            texto_game_over = self.fuente.render("Game Over! Presiona R para reiniciar", True, BLANCO)
            self.pantalla.blit(texto_game_over, (ANCHO // 2 - 200, ALTO // 2))
        
        pygame.display.flip()
        self.reloj.tick(FPS)
        return True

async def main():
    juego = SnakeGame()
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