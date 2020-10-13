class Player:
    def __init__(self, image, location):
        self.image = image
        self.location = location
        self.rect = image.get_rect(topleft=location)
        self.rect.center = location

    def move(self, direction):
        print("we got here bois")
        commands = {
            "up": (self.rect.center[0], self.rect.center[1] - 5),
            "down": (self.rect.center[0], self.rect.center[1] + 5),
            "left": (self.rect.center[0] - 5, self.rect.center[1]),
            "right": (self.rect.center[0] + 5, self.rect.center[1])
        }
        if direction not in commands: return
        self.rect.center = commands[direction]

    def draw(self, screen):
        screen.blit(self.image, self.rect)