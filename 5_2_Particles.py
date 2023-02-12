# Simple pygame program

# import this package
import pygame  # in terminal: pip3 install pygame --pre

# Format a game window:
background_colour = (255, 255, 255)  # white
(width, height) = (300, 200)  # size (pixels)
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)

# Name the window with a caption
pygame.display.set_caption('Tutorial 1')

# Drawing

class Particle:  # a class, creates a new type of object where common features are stored.
    def __init__(self, position, size):  # __init__ is a built-in function used for creating a class.
        self.x, self.y = position  # "self" is used to specify objects of a class.
        self.size = size
        self.colour = (0, 0, 255)  # blue
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

my_first_particle = Particle((150, 50), 15)  # arguments: Particle((x,y), radius)
my_first_particle.display()  # display the image of the particle

# use the flip command to display the window/screen.
pygame.display.flip()

# To keep the window closed till we close it.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

