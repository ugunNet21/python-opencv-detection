import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Konstanta
WIDTH, HEIGHT = 800, 600
ROAD_WIDTH = 400
LANE_WIDTH = ROAD_WIDTH // 2
FPS = 60

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
RED = (255, 0, 0)

# Membuat layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

# Load assets
car_img = pygame.image.load("car.jpeg")  # Ganti dengan gambar mobil
car_img = pygame.transform.scale(car_img, (50, 100))

# Posisi awal mobil
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 150
car_speed = 5

# Obstacle (Mobil Lawan)
obstacle_width = 50
obstacle_height = 100
obstacles = []
for _ in range(3):
    obstacles.append([
        random.choice([WIDTH//2 - LANE_WIDTH//2 - 25, WIDTH//2 + LANE_WIDTH//2 - 25]),
        random.randint(-600, -100),
        random.choice([-2, 0, 2])  # AI gerak ke kiri/kanan
    ])
obstacle_speed = 5

# Efek jalan bergerak
road_scroll = 0
road_speed = 5

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(GRAY)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kontrol mobil pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > WIDTH//2 - LANE_WIDTH:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH//2 + LANE_WIDTH - 50:
        car_x += car_speed
    
    # Efek jalan bergerak
    road_scroll += road_speed
    if road_scroll >= HEIGHT:
        road_scroll = 0
    
    # Menggambar jalan
    pygame.draw.rect(screen, BLACK, (WIDTH//2 - ROAD_WIDTH//2, 0, ROAD_WIDTH, HEIGHT))
    pygame.draw.line(screen, WHITE, (WIDTH//2 - LANE_WIDTH//2, 0), (WIDTH//2 - LANE_WIDTH//2, HEIGHT), 5)
    pygame.draw.line(screen, WHITE, (WIDTH//2 + LANE_WIDTH//2, 0), (WIDTH//2 + LANE_WIDTH//2, HEIGHT), 5)
    
    # Menggambar mobil pemain
    screen.blit(car_img, (car_x, car_y))
    
    # Menggerakkan dan menggambar rintangan (mobil lawan)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))
        obstacle[1] += obstacle_speed
        obstacle[0] += obstacle[2]  # Gerakan AI ke kiri/kanan
        
        # Batas gerakan AI lawan agar tetap di jalurnya
        if obstacle[0] < WIDTH//2 - LANE_WIDTH//2 - 25 or obstacle[0] > WIDTH//2 + LANE_WIDTH//2 - 25:
            obstacle[2] *= -1
        
        # Reset posisi lawan jika sudah keluar layar
        if obstacle[1] > HEIGHT:
            obstacle[1] = random.randint(-600, -100)
            obstacle[0] = random.choice([WIDTH//2 - LANE_WIDTH//2 - 25, WIDTH//2 + LANE_WIDTH//2 - 25])
            obstacle[2] = random.choice([-2, 0, 2])
        
        # Deteksi tabrakan
        if (car_x < obstacle[0] + obstacle_width and car_x + 50 > obstacle[0] and
                car_y < obstacle[1] + obstacle_height and car_y + 100 > obstacle[1]):
            print("Game Over!")
            running = False
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()