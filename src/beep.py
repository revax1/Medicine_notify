import pygame
import time

def beep_audio():
    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Set the duration to 1 minute (60,000 milliseconds)

    pygame.mixer.init()
    pygame.mixer.music.load("beep.mp3")
    pygame.mixer.music.play()
    time.sleep(3)

    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        clock.tick(1)

    # Clean up Pygame
    pygame.mixer.quit()
    pygame.quit()

beep_audio()
