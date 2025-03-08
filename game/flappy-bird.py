import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 400
screen_height = 600

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Layar
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)

# Variabel global
high_score = 0

# Fungsi untuk menampilkan teks di tengah layar
def draw_text(text, font, color, y_offset=0):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + y_offset))
    screen.blit(text_surface, text_rect)

# Fungsi untuk menampilkan skor
def show_score(score):
    score_text = small_font.render(f"Score: {score}", True, black)
    screen.blit(score_text, [10, 10])

# Fungsi untuk menggambar pipa
def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, blue, pipe)

# Fungsi utama game
def game_loop(level):
    global high_score

    # Posisi awal burung
    bird_x = 50
    bird_y = 300
    bird_velocity = 0
    gravity = 0.5

    # Pipa
    pipe_width = 70
    pipe_height = random.randint(150, 400)
    pipe_gap = 150
    pipe_x = screen_width
    pipes = []

    # Skor
    score = 0

    # Kecepatan pipa berdasarkan level
    pipe_speed = 5 + level * 2

    # Game loop
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Tombol panah atas untuk terbang ke atas
                    bird_velocity = -10
                if event.key == pygame.K_DOWN:  # Tombol panah bawah untuk terbang ke bawah
                    bird_velocity = 10

        # Gerakan burung
        bird_velocity += gravity
        bird_y += bird_velocity

        # Gerakan pipa
        if len(pipes) == 0 or pipes[-1].x < screen_width - 200:
            pipe_height = random.randint(150, 400)
            pipes.append(pygame.Rect(pipe_x, 0, pipe_width, pipe_height))
            pipes.append(pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, screen_height - pipe_height - pipe_gap))

        for pipe in pipes:
            pipe.x -= pipe_speed
            if pipe.x + pipe.width < 0:
                pipes.remove(pipe)
                if pipe.y == 0:
                    score += 1

        # Cek tabrakan
        bird_rect = pygame.Rect(bird_x, bird_y, 40, 40)
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                game_over = True

        if bird_y > screen_height or bird_y < 0:
            game_over = True

        # Gambar layar
        screen.fill(white)
        pygame.draw.rect(screen, black, bird_rect)
        draw_pipes(pipes)
        show_score(score)
        pygame.display.update()

        # Frame rate
        clock.tick(30)

    # Update high score
    if score > high_score:
        high_score = score

    # Game over screen
    game_over_screen(score)

# Fungsi untuk menampilkan layar game over
def game_over_screen(score):
    while True:
        screen.fill(white)
        draw_text("Game Over", font, red, -50)
        draw_text(f"Score: {score}", small_font, black, 0)
        draw_text(f"High Score: {high_score}", small_font, black, 50)
        draw_text("Press SPACE to Restart", small_font, black, 100)
        draw_text("Press M for Menu", small_font, black, 150)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop(1)  # Mulai kembali dengan level 1
                if event.key == pygame.K_m:
                    main_menu()

# Fungsi untuk menampilkan menu utama
def main_menu():
    while True:
        screen.fill(white)
        draw_text("Flappy Bird", font, blue, -100)
        draw_text("1. Level Easy", small_font, black, -50)
        draw_text("2. Level Medium", small_font, black, 0)
        draw_text("3. Level Hard", small_font, black, 50)
        draw_text("Press Q to Quit", small_font, black, 150)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop(1)  # Level Easy
                if event.key == pygame.K_2:
                    game_loop(2)  # Level Medium
                if event.key == pygame.K_3:
                    game_loop(3)  # Level Hard
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# Jalankan menu utama
main_menu()