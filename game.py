import pygame
import settings
from snake import Snake
from food import Food
import ui
from logger import log


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.snake = Snake()
        self.food = Food()

        self.score = 0
        self.high_score = 0

        self.state = "START"

    def reset(self):
        self.snake.reset()
        self.food.respawn()
        self.score = 0
        self.state = "RUNNING"
        log("Game restarted")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if self.state == "START" and event.key == pygame.K_SPACE:
                    self.reset()

                elif self.state == "GAME_OVER" and event.key == pygame.K_r:
                    self.reset()

                elif self.state == "RUNNING":
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((1, 0))
        return True

    def update(self):
        if self.state != "RUNNING":
            return

        self.snake.move()

        # Food collision
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.respawn()
            self.score += 1
            log(f"Score: {self.score}")

        head_x, head_y = self.snake.body[0]

        # Wall collision
        if (
            head_x < 0
            or head_x >= settings.WIDTH // settings.GRID_SIZE
            or head_y < 0
            or head_y >= settings.HEIGHT // settings.GRID_SIZE
        ):
            self.state = "GAME_OVER"
            self.high_score = max(self.high_score, self.score)

        # Self collision
        if self.snake.check_self_collision():
            self.state = "GAME_OVER"
            self.high_score = max(self.high_score, self.score)

    def draw(self):
        if self.state == "START":
            ui.start_screen(self.screen)
            return

        if self.state == "GAME_OVER":
            ui.game_over_screen(self.screen, self.score, self.high_score)
            return

        # Background
        self.screen.fill(settings.BLACK)

        # Draw snake (head + body color difference)
        for i, segment in enumerate(self.snake.body):
            color = settings.GREEN if i == 0 else settings.DARK_GREEN

            pygame.draw.rect(
                self.screen,
                color,
                (
                    segment[0] * settings.GRID_SIZE,
                    segment[1] * settings.GRID_SIZE,
                    settings.GRID_SIZE,
                    settings.GRID_SIZE,
                ),
            )

        # Draw food
        fx, fy = self.food.position
        rect = pygame.Rect(
            fx * settings.GRID_SIZE,
            fy * settings.GRID_SIZE,
            settings.GRID_SIZE,
            settings.GRID_SIZE,
        )

        pygame.draw.rect(self.screen, settings.RED, rect)
        pygame.draw.rect(self.screen, settings.WHITE, rect, 2)  # border

        # Score
        ui.draw_text_center(self.screen, f"Score: {self.score}", 30, ui.TEXT_FONT)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.clock.tick(settings.FPS)
            running = self.handle_events()
            self.update()
            self.draw()

        pygame.quit()