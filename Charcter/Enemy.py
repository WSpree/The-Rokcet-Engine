from Charcter import Charcter
class Enemy(Charcter):
    def __init__(self, health, speed, spawnLocation, x, y):
        super().__init__(health, speed, spawnLocation, x, y)