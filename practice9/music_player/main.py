import pygame
from player import MusicPlayer

# Initialize pygame
pygame.init()

# Set up display
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("WAV Music Player")

# Set up font for track display
font = pygame.font.SysFont("Arial", 20)

# Create music player object
player = MusicPlayer()

# Function to display current track and progress
def display_ui():
    screen.fill((0, 0, 0))  # Fill screen with black

    # Display current track
    track_text = font.render(f"Current Track: {player.get_current_track()}", True, (255, 255, 255))
    screen.blit(track_text, (20, 20))

    # Display playback progress
    progress_text = font.render(f"Progress: {player.get_progress():.2f}s", True, (255, 255, 255))
    screen.blit(progress_text, (20, 50))

    pygame.display.update()

# Main game loop
running = True
while running:
    display_ui()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                player.play()
            elif event.key == pygame.K_s:  # Stop
                player.stop()
            elif event.key == pygame.K_n:  # Next track
                player.next_track()
            elif event.key == pygame.K_b:  # Previous track
                player.previous_track()
            elif event.key == pygame.K_q:  # Quit
                running = False

    pygame.time.Clock().tick(60)  # Limit FPS to 60

pygame.quit()