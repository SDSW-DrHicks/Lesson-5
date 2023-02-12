# Simple pygame screen

# import this package
import pygame # in terminal: pip3 install pygame -pre

# Format a game window:
background_colour = (255,255,255) # white
(width, height) = (300, 200) # size (pixels)
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)

# Name the window with a caption
pygame.display.set_caption('Tutorial 1')

# use the flip command to display the window/screen.
pygame.display.flip()

# To keep the window closed till we close it.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()