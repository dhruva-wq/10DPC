#Day 10 practice

#Assignment

import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen size
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_size = 20
snake_speed = 10

font = pygame.font.SysFont(None, 30)


def show_score(score):
    value = font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, (10, 10))


def message(text, color):
    msg = font.render(text, True, color)
    screen.blit(msg, (150, HEIGHT // 2))


def game():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2

    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - snake_size) / 20.0) * 20
    food_y = round(random.randrange(0, HEIGHT - snake_size) / 20.0) * 20

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press C to Play Again or Q to Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        # FIX: reset the round instead of recursively
                        # calling game(). Recursion + pygame.quit() at
                        # the end was tearing down the display while
                        # the outer call was still running.
                        x = WIDTH // 2
                        y = HEIGHT // 2
                        x_change = 0
                        y_change = 0
                        snake = []
                        snake_length = 1
                        food_x = round(random.randrange(0, WIDTH - snake_size) / 20.0) * 20
                        food_y = round(random.randrange(0, HEIGHT - snake_size) / 20.0) * 20
                        game_close = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0

                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0

                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0

        x += x_change
        y += y_change

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(BLACK)

        pygame.draw.rect(screen, GREEN, [food_x, food_y, snake_size, snake_size])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)

        snake.append(snake_head)

        if len(snake) > snake_length:
            del snake[0]

        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

        for block in snake:
            pygame.draw.rect(screen, WHITE, [block[0], block[1], snake_size, snake_size])

        show_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_size) / 20.0) * 20
            food_y = round(random.randrange(0, HEIGHT - snake_size) / 20.0) * 20
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()


game()