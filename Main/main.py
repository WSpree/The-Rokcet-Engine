import pygame
from Terrain.Terrain import Terrain
from Charcter.Player import Player
from Constats import *

background_colour = (255, 255, 255)
(width, height) = (900, 900)

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF, 32)
clock = pygame.time.Clock()

pygame.display.set_caption('Rocket Engine')
screen.fill(background_colour)
pygame.display.flip()

gray = (125, 125, 125)
pygame.draw.rect(screen, gray, (0, 0, 900, 100)) #Top
pygame.draw.rect(screen, gray, (0, 0, 150, 900)) #Left
pygame.draw.rect(screen, gray, (750, 0, 150, 900)) #Right
pygame.draw.rect(screen, gray, (0, 700, 900, 200)) #Bottom

entities = []
entities.append(Player(tree, (100, 100)))

running = True
edit = True

def controls (edit, entities):
  if edit == True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
          pos = pygame.mouse.get_pos()
          pygame.draw.rect(screen, (255, 0, 0), (pos[0], pos[1], 20, 20))
        elif mouse_pressed[2]:
          edit = False

  else:
    held = [0, 0, 0, 0] #left, right, up, down
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[2]:
          edit = True
      elif event.type == pygame.KEYDOWN:
        if event.type == pygame.K_LEFT:
          held[0] = 1
        if event.type == pygame.K_RIGHT:
          held[1] = 1
        if event.type == pygame.K_UP:
          held[2] = 1
        if event.type == pygame.K_DOWN:
          held[3] = 1
      elif event.type == pygame.KEYUP:
        if event.type == pygame.K_LEFT:
          held[0] = 0
        if event.type == pygame.K_RIGHT:
          held[1] = 0
        if event.type == pygame.K_UP:
          held[2] = 0
        if event.type == pygame.K_DOWN:
          held[3] = 0

    for key in held:
      if key:
        dir = ["left", "right", "up", "down"]
        print("we got here")
        entity[0].move(dir[entities.indexOf(key)])

  return True

while running:
  running = controls(edit, entities)

  for entity in entities:
    entity.draw(screen)
  pygame.display.update()