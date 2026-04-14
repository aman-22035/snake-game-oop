import random
from settings import WIDTH, HEIGHT, GRID_SIZE # constraints

class Food:
    def __init__(self):
        self.position = self.generate_food()

    def generate_food(self):
        x = random.randint(0, (WIDTH // GRID_SIZE) -1) 
        y = random.randint(0, (HEIGHT // GRID_SIZE) -1)
        return (x, y)
        # basically we are generating random x and y coordinate for food where
        # x and y are between 0 and the number of grid cells in width and height respectively.

    def respawn(self):
        self.position = self.generate_food() 
        # when snake eats the food we need to generate new food at random position.