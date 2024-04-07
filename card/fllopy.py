import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.25
FLAP_POWER = -8
PIPE_GAP = 150
PIPE_SPEED = 3

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Floppy Bird")

# Load images
bird_img = pygame.image.load("bird.png")
pipe_img = pygame.image.load("pipe.png")

# Scale images
bird_img = pygame.transform.scale(bird_img, (50, 50))
pipe_img = pygame.transform.scale(pipe_img, (50, HEIGHT))

# Define classes
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.vel_y = 0

    def flap(self):
        self.vel_y = FLAP_POWER

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.y = random.randint(100, HEIGHT - PIPE_GAP - 100)

    def update(self):
        self.x -= PIPE_SPEED

    def off_screen(self):
        return self.x < -50

    def draw(self):
        screen.blit(pipe_img, (self.x, 0))
        screen.blit(pipe_img, (self.x, self.y + PIPE_GAP))

# Create objects
bird = Bird()
pipes = []

# Game loop
clock = pygame.time.Clock()
score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()

    # Update
    bird.update()
    if len(pipes) == 0 or pipes[-1].x < WIDTH - 200:
        pipes.append(Pipe())
    for pipe in pipes:
        pipe.update()
        if pipe.off_screen():
            pipes.remove(pipe)
            score += 1
    if bird.y < 0 or bird.y > HEIGHT - 50:
        running = False
    for pipe in pipes:
        if pipe.x < bird.x + 50 and pipe.x + 50 > bird.x:
            if bird.y < pipe.y or bird.y > pipe.y + PIPE_GAP:
                running = False

    # Draw
    screen.fill(WHITE)
    bird.draw()
    for pipe in pipes:
        pipe.draw()

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
