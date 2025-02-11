import pygame
import random
import threading

pygame.init()
# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rainbow")

def random_color():
  return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))


def noise(Input):
  if Input < 50:
    result = Input + random.randint(0, 0)
  else:
    result = Input + random.randint(0, 0)
  return max(50, min(255, result))


class Rainbow():
    def __init__(self, x, y,GX,GY):
        self.x = x
        self.y = y
        self.GX = GX
        self.GY = GY
        self.color = random_color()
        self.buds = [] #buds means buddys 
        self.blend_lock = threading.Lock()


    def draw(self):
      pygame.draw.rect(screen, self.color, (self.x, self.y, 5, 5))



    def get_color(self):
      return self.color

    def get_buds(self):
      if self.GY + 1 < len(grid):
        self.buds.append(grid[self.GY + 1][self.GX])
      if self.GY - 1 >= 0:
        self.buds.append(grid[self.GY - 1][self.GX])
      if self.GX + 1 < len(grid[0]):
        self.buds.append(grid[self.GY][self.GX + 1])
      if self.GX - 1 >= 0:
        self.buds.append(grid[self.GY][self.GX - 1])
      #print(self.buds)


    def blend(self):
      with self.blend_lock:
        if random.random() < 0.1:  # Only blend 10% of the time
            bud_color_1 = []
            bud_color_2 = []
            bud_color_3 = []
            for bud in self.buds:
                bud_color_1.append(bud.get_color()[0])
                bud_color_2.append(bud.get_color()[1])
                bud_color_3.append(bud.get_color()[2])
            self.color = (
                noise(random.choice(bud_color_1)),
                noise(random.choice(bud_color_2)),
                noise(random.choice(bud_color_3))
              )











E = []
grid_width = screen.get_width() // 5
grid_height = screen.get_height() // 5
grid = []
for _ in range(grid_height):
    grid.append([None] * grid_width)

for j in range(grid_height):
  for i in range(grid_width):
      rainbow = Rainbow(i * 5, j * 5, i, j)
      grid[j][i] = rainbow
      E.append(rainbow)


for i in E:
  i.get_buds()

running = True
clock = pygame.time.Clock()

# Thread to handle blending
def blend_thread():

    while running:
        for i in E:
            i.blend()
blend_threead = threading.Thread(target=blend_thread)
blend_threead.start()

pygame.time.wait(2000)
while running:

    screen.fill((0, 0, 0))
    for i in E:
        i.draw()
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
