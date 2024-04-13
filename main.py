import pygame
import random
import math

pygame.init()

FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187,173,160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205,192,180)
FONT_COLOR = (119,110,101)


FONT = pygame.font.SysFont("Comic Sans",60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

class Tile: 
    COLORS = [
        (237,229,218),
        (238,225,201),
        (243,178,122),
        (246,150,101),
        (247,124,95),
        (247,95,59),
        (237,208,115),
        (237,204,99),
        (236,202,80),
    ]
    
    def __init__(self,value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        color = self.COLORS[color_index]
        return color
    
    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(WINDOW, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))
        
        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            
            text, 
                (
                        self.x + (RECT_WIDTH/ 2 - text.get_width()/2),
                        self.y + (RECT_HEIGHT/ 2 - text.get_height()/2),
                   
                   ),
                )
    
    def set_pos(self):
        pass
    
    def move(self, delta):
        pass
def draw_grid(window):
    for row in range(1,ROWS): # Horizontal grid
        y = row * RECT_HEIGHT
        pygame.draw.line(window,OUTLINE_COLOR, (0,y), (WIDTH, y), OUTLINE_THICKNESS)
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)
    
    
    for col in range(1,COLS): # Vertical grid
        x = col * RECT_WIDTH
        pygame.draw.line(window,OUTLINE_COLOR, (x,0), (x, HEIGHT), OUTLINE_THICKNESS)
    
    
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)
    
    for tile in tiles.values():
        tile.draw(window)
    
    draw_grid(window)
    pygame.display.update() # override whatever on screen
    
def get_random_pos(tiles):
    row = None
    col = None
    while True:
        row = random.randrange(0, ROWS) # random from 0 - No. of ROWS
        col = random.randrange(0, COLS)
        
        if f"{row}{col}" not in tiles:
            break
        
    return row, col
def generate_tiles():
    tiles = {}
    for _ in range(2): # '_' used to replace anything any variables like 'i'
        row, col = get_random_pos(tiles)  # get_random_pos used to get any row and column that didn't already exists
        tiles[f"{row}{col}"] = Tile(2, row, col)
    return tiles

def main(window):
    clock = pygame.time.Clock()
    run = True
    tiles = {"00": Tile(4, 0, 0), "20": Tile(128, 2, 0), "02" :Tile(64, 0, 2)}
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, tiles)
    
    pygame.quit()
    
if __name__ == "__main__":
    main(WINDOW)