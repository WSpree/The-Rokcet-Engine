class Terrain():
    def __init__(self, image, location, size):
        self.image = image
        self.location = location
        self.size = size
        self.rect = image.get_rect(topleft=(150, 300))

    def move(self, x, y, dir):
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)