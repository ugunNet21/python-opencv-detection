import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PLAYER_SPEED = 5
ENEMY_SPEED = 3
NUM_PLAYERS = 3
NUM_ENEMIES = 4

# Create Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gobak Sodor")

# Load Assets
font = pygame.font.Font(None, 36)

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.rect.clamp_ip(screen.get_rect())

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.direction * ENEMY_SPEED
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.direction *= -1

# Obstacle Class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Setup Game
players = pygame.sprite.Group()
for i in range(NUM_PLAYERS):
    players.add(Player(50, HEIGHT // (NUM_PLAYERS + 1) * (i + 1), BLUE))

enemies = pygame.sprite.Group()
for i in range(NUM_ENEMIES):
    enemies.add(Enemy(WIDTH // 6 * (i % 5 + 1), HEIGHT // (NUM_ENEMIES // 2 + 1) * ((i % 2) + 1)))

obstacles = pygame.sprite.Group()
for i in range(5):
    obstacles.add(Obstacle(WIDTH // 6 * (i+1), 100, 20, 400))

all_sprites = pygame.sprite.Group()
all_sprites.add(players)
all_sprites.add(obstacles)
all_sprites.add(enemies)

# Score & Level
score = 0
level = 1

def reset_game():
    global score, level
    score = 0
    level = 1
    for player in players:
        player.rect.topleft = (50, HEIGHT // (NUM_PLAYERS + 1) * (list(players).index(player) + 1))

# Game Loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            for player in players:
                if event.key == pygame.K_LEFT:
                    player.speed_x = -PLAYER_SPEED
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = PLAYER_SPEED
                elif event.key == pygame.K_UP:
                    player.speed_y = -PLAYER_SPEED
                elif event.key == pygame.K_DOWN:
                    player.speed_y = PLAYER_SPEED
        elif event.type == pygame.KEYUP:
            for player in players:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player.speed_x = 0
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    player.speed_y = 0
    
    # Update
    all_sprites.update()
    
    # Check collision with obstacles and enemies
    for player in players:
        if pygame.sprite.spritecollide(player, obstacles, False) or pygame.sprite.spritecollide(player, enemies, False):
            reset_game()
    
    # Check if all players reach the goal
    if all(player.rect.right >= WIDTH - 10 for player in players):
        score += 1
        level += 1
        for player in players:
            player.rect.topleft = (50, HEIGHT // (NUM_PLAYERS + 1) * (list(players).index(player) + 1))
        enemies.add(Enemy(WIDTH // 6 * level, HEIGHT // 3))
        enemies.add(Enemy(WIDTH // 6 * level, HEIGHT // 1.5))
    
    # Draw
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score} | Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
