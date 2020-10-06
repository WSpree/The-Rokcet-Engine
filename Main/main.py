import pygame

background_colour = (255, 255, 255)
(width, height) = (900, 900)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
gray = (125, 125, 125)
pygame.draw.rect(screen, gray, (0, 0, 900, 100)) #Top
pygame.draw.rect(screen, gray, (0, 0, 150, 900)) #Left
pygame.draw.rect(screen, gray, (750, 0, 150, 900)) #Right
pygame.draw.rect(screen, gray, (0, 700, 900, 200)) #Bottom

running = True
edit = True

while running:
  if edit == True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    pygame.display.update()
  else:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    pygame.display.update()