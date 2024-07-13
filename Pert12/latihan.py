import pygame
import random
from pygame.locals import *

class Ball():
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()

        self.maxWidth = windowWidth - self.rect.width
        self.maxHeight = windowHeight - self.rect.height

        self.x = windowWidth // 2
        self.y = windowHeight // 2

        speedList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedList)
        self.ySpeed = random.choice(speedList)

    def update(self):
        # Update posisi bola berdasarkan kecepatan
        self.x += self.xSpeed
        self.y += self.ySpeed

        # Memantulkan bola jika mencapai batas layar
        if self.x <= 0 or self.x >= self.maxWidth:
            self.xSpeed = -self.xSpeed
        if self.y <= 0 or self.y >= self.maxHeight:
            self.ySpeed = -self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

def draw_text(surface, text, size, x, y, color):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

# Inisialisasi Pygame
pygame.init()

# Set up layar dan window
windowWidth = 800
windowHeight = 600
window = pygame.display.set_mode((windowWidth, windowHeight), RESIZABLE)
pygame.display.set_caption('Bouncing Ball')

# Warna latar belakang
backgroundColor = (0, 0, 0)  # Warna hitam

# Load gambar bola
ball = Ball(window, windowWidth, windowHeight)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == VIDEORESIZE:
            # Tangani perubahan ukuran jendela
            windowWidth = event.w
            windowHeight = event.h
            window = pygame.display.set_mode((windowWidth, windowHeight), RESIZABLE)
            ball.maxWidth = windowWidth - ball.rect.width
            ball.maxHeight = windowHeight - ball.rect.height

    # Bersihkan layar dengan warna latar belakang
    window.fill(backgroundColor)

    # Gambar teks "vandy wota" dengan ukuran yang menyesuaikan
    text_size = min(windowWidth // 10, windowHeight // 10)
    draw_text(window, "VANDY WOTA", text_size, windowWidth // 2, windowHeight // 2, (255, 255, 255))

    # Perbarui dan gambar bola
    ball.update()
    ball.draw()

    # Perbarui layar
    pygame.display.flip()

    # Atur frame rate
    clock.tick(60)

pygame.quit()
