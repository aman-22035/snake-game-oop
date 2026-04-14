import pygame
import settings

pygame.font.init()

TITLE_FONT = pygame.font.SysFont("Arial", 50)
TEXT_FONT = pygame.font.SysFont("Arial", 30)


def draw_text_center(screen, text, y, font, color=settings.GREEN):
    label = font.render(text, True, color)
    rect = label.get_rect(center=(settings.WIDTH // 2, y))
    screen.blit(label, rect)


def start_screen(screen):
    screen.fill(settings.BLACK)

    draw_text_center(screen, "SNAKE GAME", 180, TITLE_FONT)
    draw_text_center(screen, "Press SPACE to Start", 300, TEXT_FONT)
    draw_text_center(screen, "Use Arrow Keys to Move", 350, TEXT_FONT)

    pygame.display.flip()


def game_over_screen(screen, score, high_score):
    screen.fill(settings.BLACK)

    draw_text_center(screen, "GAME OVER", 160, TITLE_FONT)
    draw_text_center(screen, f"Score: {score}", 240, TEXT_FONT)
    draw_text_center(screen, f"High Score: {high_score}", 280, TEXT_FONT)
    draw_text_center(screen, "Press R to Restart", 340, TEXT_FONT)

    pygame.display.flip()