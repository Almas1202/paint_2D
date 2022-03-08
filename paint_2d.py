import pygame

#Настройки окна
WIDTH = 500
HEIGHT = 500
FPS = 60

#Настройка цвета
WHITE = (255, 255, 255)
RED = (241, 58, 19)
GREEN=(60, 210, 100)
BLUE=(20, 80, 210)
BLACK = (0, 0, 0)
YELLOW = (255, 202, 24)
BROWN = (150, 72, 27)
DARK_GREEN = (16, 112, 43)
SKY_BLUE = (0, 168, 243)


GREY = (71, 74, 81)
WHITE_1 = (230, 235, 190)

rows = cols = 50

pixel_s = WIDTH//rows

drawing_color = BLACK

button = 25
#Инициализация
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")


#Функции

def draw(screen, grid):
    screen.fill(WHITE)
    draw_grid(screen, grid)
    pygame.draw.rect(screen, GREY, (0, 400, 500, 100))
    

def init_grid(rows, cols, color):
    grid = []
    
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)
    return grid

def draw_grid(screen, grid):
    for i, row in enumerate(grid):
        for j, pixel_color in enumerate(row):
            pygame.draw.rect(screen, pixel_color, (j * pixel_s, i * pixel_s, pixel_s, pixel_s))
    
    pygame.draw.line(screen, BLACK, (1, 1), (1, 499))
    pygame.draw.line(screen, BLACK, (1, 1), (499, 1))
    pygame.draw.line(screen, BLACK, (499, 1), (499, 499))
    pygame.draw.line(screen, BLACK, (1, 499), (499, 499))
    
    if grid_lines == True:
        for i in range(rows + 1):
            pygame.draw.line(screen, BLACK, (0, i * pixel_s),(WIDTH, i * pixel_s))
        for i in range(cols + 1):
            pygame.draw.line(screen, BLACK, (i * pixel_s, 0),(i * pixel_s, WIDTH - 100))
def grid_pos(pos):
    x, y = pos
    row = y // pixel_s
    col = x // pixel_s

    return row, col

font = pygame.font.SysFont('arial', 10)
text = font.render("Стерка", 1, BLACK)
text1 = font.render("Сетка:", 1, BLACK)
text11 = font.render("ВКЛ", 1, BLACK)
text2 = font.render("Сетка:", 1, BLACK)
text22 = font.render("ВЫКЛ", 1, BLACK)

grid = init_grid(rows, cols, WHITE)
running = True      
grid_lines = False
drawing = False
big_brush = False
net = False
while running:
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] > 30 and pos[0] < 55 and pos[1] > 425 and pos[1] < 425 + button:
                    drawing_color = BLACK
                    
                if pos[0] > 65 and pos[0] < 90 and pos[1] > 425 and pos[1] < 425 + button:
                    drawing_color = RED
                
                if pos[0] > 30 and pos[0] < 55 and pos[1] > 460 and pos[1] < 460 + button:
                    drawing_color = GREEN
                
                if pos[0] > 65 and pos[0] < 90 and pos[1] > 460 and pos[1] < 460 + button:
                    drawing_color = BLUE
                
                if pos[0] > 370 and pos[0] < 420 and pos[1] > 425 and pos[1] < 425 + 50:
                    drawing_color = WHITE
                
                if pos[0] > 100 and pos[0] < 125 and pos[1] > 425 and pos[1] < 425 + button:
                    drawing_color = YELLOW
                    
                if pos[0] > 100 and pos[0] < 125 and pos[1] > 460 and pos[1] < 460 + button:
                    drawing_color = BROWN
                
                if pos[0] > 135 and pos[0] < 160 and pos[1] > 425 and pos[1] < 425 + button:
                    drawing_color = SKY_BLUE
                
                if pos[0] > 135 and pos[0] < 160 and pos[1] > 460 and pos[1] < 460 + button:
                    drawing_color = DARK_GREEN
                
                if pos[0] > 300 and pos[0] < 350 and pos[1] > 425 and pos[1] < 425 + 50:
                    grid_lines = True
                
                if pos[0] > 230 and pos[0] < 280 and pos[1] > 425 and pos[1] < 425 + 50:
                    grid_lines = False

                if pos[0] > 440 and pos[0] < 480 and pos[1] > 415 and pos[1] < 415 + 40:
                    big_brush = True
                
                if pos[0] > 440 and pos[0] < 480 and pos[1] > 465 and pos[1] < 475:
                    big_brush = False
                
                if pos[0] > 0 and pos[0] < WIDTH and pos[1] > 0 and pos[1] < 400:  
                    drawing = True
                
        if i.type == pygame.MOUSEBUTTONUP:
            if i.button == 1:
                drawing = False
    if drawing == True:
        pos = pygame.mouse.get_pos()
                
        x, y = pos
        row, col = grid_pos(pos)
        if big_brush == False:
            grid[row][col] = drawing_color

        if big_brush == True:
            grid[row][col] = drawing_color
            grid[row-1][col] = drawing_color
            grid[row][col-1] = drawing_color
            grid[row-1][col-1] = drawing_color

    draw(screen, grid)

    #Кнопки
    pygame.draw.rect(screen, BLACK, (30, 425, button, button))
    pygame.draw.rect(screen, GREEN, (30, 460, button, button))
    pygame.draw.rect(screen, BLUE, (65, 460, button, button))
    pygame.draw.rect(screen, RED, (65, 425, button, button))
    pygame.draw.rect(screen, YELLOW, (100, 425, button, button))
    pygame.draw.rect(screen, BROWN, (100, 460, button, button))
    pygame.draw.rect(screen, SKY_BLUE, (135, 425, button, button))
    pygame.draw.rect(screen, DARK_GREEN, (135, 460, button, button))
    
    pygame.draw.rect(screen, WHITE_1, (370, 425, 50, 50))
    pygame.draw.rect(screen, WHITE_1, (300, 425, 50, 50))
    pygame.draw.rect(screen, WHITE_1, (230, 425, 50, 50))
    
    pygame.draw.rect(screen, BLACK, (440, 430, 40, 10))
    pygame.draw.rect(screen, BLACK, (455, 415, 10, 40))
    
    pygame.draw.rect(screen, BLACK, (440, 465, 40, 10))
    
    screen.blit(text, (375, 435))
    screen.blit(text1, (305, 435))
    screen.blit(text11, (310, 448))
    
    screen.blit(text2, (235, 435))
    screen.blit(text22, (240, 448))
    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()