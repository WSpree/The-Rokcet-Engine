from Main import Map


class Charcter(Map):
    def __init__(self, health, speed, spawnLocation):
        self.health = health
        self.speed = speed
        self.spawnLocation = spawnLocation