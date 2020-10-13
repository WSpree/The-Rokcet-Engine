import os
import pygame
import random

def load(file_name):
    return pygame.image.load(os.path.join("Assets", file_name))

def scale(file, size):
    return pygame.transform.scale(file, size)

tree = scale(load("tree1.png"), (100, 130))
