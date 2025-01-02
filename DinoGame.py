
# Game speed variables
INITIAL_SPEED = 5
SPEED_INCREASE = 0.1
MAX_SPEED = 15
game_speed = INITIAL_SPEED

import pygame
import random
import time
import math

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dinosaur Hopping Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Dinosaur properties
dino_width = 50
dino_height = 50
dino_x = 100
dino_y = WINDOW_HEIGHT - dino_height
dino_velocity = 0
GRAVITY = 0.8
JUMP_FORCE = -15

# Obstacle properties
obstacle_width = 30
obstacle_height = 50
obstacle_x = WINDOW_WIDTH
obstacle_y = WINDOW_HEIGHT - obstacle_height
obstacle_speed = game_speed  # Use game_speed instead of fixed speed

# Game variables
score = 0
game_over = False
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino_y >= WINDOW_HEIGHT - dino_height:
                dino_velocity = JUMP_FORCE
            if event.key == pygame.K_r and game_over:
                # Reset game
                game_over = False
                score = 0
                obstacle_x = WINDOW_WIDTH
                dino_y = WINDOW_HEIGHT - dino_height
                dino_velocity = 0
                game_speed = INITIAL_SPEED  # Reset game speed

    if not game_over:
        # Update dinosaur position
        dino_velocity += GRAVITY
        dino_y += dino_velocity
        if dino_y > WINDOW_HEIGHT - dino_height:
            dino_y = WINDOW_HEIGHT - dino_height
            dino_velocity = 0

        # Update obstacle position and game speed
        obstacle_x -= game_speed  # Use game_speed instead of obstacle_speed
        if obstacle_x < -obstacle_width:
            obstacle_x = WINDOW_WIDTH
            score += 1
            # Increase game speed with each obstacle cleared
            game_speed = min(game_speed + SPEED_INCREASE, MAX_SPEED)

        # Check for collision
        dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        
        if dino_rect.colliderect(obstacle_rect):
            game_over = True

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (dino_x, dino_y, dino_width, dino_height))
    pygame.draw.rect(screen, BLACK, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))
    
    if game_over:
        game_over_text = font.render('Game Over! Press R to restart', True, BLACK)
        screen.blit(game_over_text, (WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
