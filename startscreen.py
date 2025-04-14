from constants import *
import pygame
import sys

def start_screen(screen, font):
    title_font = pygame.font.SysFont("Chalkduster", 108)
    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 40, 300, 80)

    while True:
        screen.fill((0, 0, 0))
        
        # Draw title
        title = title_font.render("ASTEROIDS", True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        # Detect hover
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            button_color = (200, 200, 200)  # lighter when hovered
        else:
            button_color = (255, 255, 255)

        # Draw button
        pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
        button_text = font.render("Start Game", True, (0, 0, 0))
        screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2,
                                  button_rect.y + (button_rect.height - button_text.get_height()) // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

