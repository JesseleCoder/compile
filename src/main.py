import pygame
import sys
from random import randint as int
# Initialize Pygame
pygame.init()
print("DVD.PY running")
# Constants
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")

###########################################################

class DVD:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.X_V = 1
        self.Y_V = 1
        self.color = (255, 0, 0)  # Initial color set to red

    def draw(self, win):    
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))  



    def wall(self,X_V,Y_V):
      ...
    def move(self):
      #right
      if self.x < 0:
        self.X_V = int(1,5)
        self.Y_V = int(-5,5)
        self.x += self.X_V
        self.color = (int(0,255),int(0,255),int(0,255))
      #left
      if self.x > WIDTH:
        self.X_V = int(-5,-1)
        self.Y_V = int(-3,3)
        self.x += self.X_V
        self.color = (int(0,255),int(0,255),int(0,255))
      #bottem
      if self.y > HEIGHT:
        self.X_V = int(-3,3)
        self.Y_V = int(-3,-1)
        self.y += self.X_V
        self.color = (int(0,255),int(0,255),int(0,255))
      #top
      if self.y < 0:
        self.X_V = int(-3,3)
        self.Y_V = int(1,3)
        self.y += self.X_V
        self.color = (int(0,255),int(0,255),int(0,255))
      else:
        self.x += self.X_V
        self.y += self.Y_V
        
     
      

        

###########################################################

# Function to draw window
def draw_window(dvd, win):
    win.fill((0, 0, 0))  # Fill the window with black color
    dvd.draw(win)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    frame_rate = 40

    dvd_data = DVD(100, 100, 25, 25)

    run = True
    while run:
        clock.tick(frame_rate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        dvd_data.move()
        
        draw_window(dvd_data, WIN)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
