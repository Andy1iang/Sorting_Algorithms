import pygame
import random
import math
pygame.init()


class ScreenInfo:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    GREY = (128, 128, 128)
    LIGHT_GREY = (170, 170, 170)
    DARK_GREY = (50, 50, 50)
    BACKGROUND_COLOR = WHITE

    SIDE_PADDING = 100
    TOP_PADDING = 100

    FONT = pygame.font.SysFont('Monocraft', 20)

    def __init__(self, width, height, arr):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Visualizer")
        self.adjustBars(arr)

    def adjustBars(self, arr):
        self.arr = arr
        self.minVal = min(arr)
        self.maxVal = max(arr)
        self.barWidth = math.floor((self.width - self.SIDE_PADDING) / len(arr))
        self.barHeight = math.floor(
            (self.height-self.TOP_PADDING)/(self.maxVal - self.minVal+1))
        self.startX = self.SIDE_PADDING // 2


def generateList(n, minVal, maxVal):
    return [random.randint(minVal, maxVal) for _ in range(n)]


def draw(screen):
    screen.window.fill(screen.BACKGROUND_COLOR)

    controls = screen.FONT.render(
        "R: Reset | Space: Sort | A: Ascending | D: Descending", 1, screen.BLACK)
    screen.window.blit(
        controls, (screen.width//2 - controls.get_width()//2, 5))

    drawBars(screen)
    pygame.display.update()


def drawBars(screen, colorPositions={}, clear=False):
    colors = [screen.LIGHT_GREY, screen.GREY, screen.DARK_GREY]
    arr = screen.arr

    if clear:
        clearRect = (screen.SIDE_PADDING//2, screen.TOP_PADDING, screen.width -
                     screen.SIDE_PADDING, screen.height - screen.TOP_PADDING)
        pygame.draw.rect(screen.window, screen.BACKGROUND_COLOR, clearRect)

    for i, val in enumerate(arr):
        x = screen.startX + i * screen.barWidth
        y = screen.height - ((val - screen.minVal) * screen.barHeight)
        color = colors[i % 3]
        if i in colorPositions:
            color = colorPositions[i]
        pygame.draw.rect(screen.window, color,
                         (x, y, screen.barWidth, screen.height))
        
    if clear:
        pygame.display.update()


def sortIt(screen, ascending):
    arr = screen.arr
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                drawBars(screen, {j: screen.GREEN, j+1: screen.RED}, True)
                yield True
    return arr


def main():

    run = True
    clock = pygame.time.Clock()
    screen = ScreenInfo(800, 600, generateList(50, 0, 100))
    sorting = False
    ascending = True
    draw(screen)

    sorter = sortIt
    sorterGen = None

    while run:
        clock.tick(60)  # 60 fps

        if sorting:
            try:
                next(sorterGen)
            except StopIteration:
                sorting = False
        else:
            draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                screen.arr = generateList(50, 0, 100)
                draw(screen)
                sorting = False

            if event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorterGen = sorter(screen, ascending)

            if event.key == pygame.K_a and not sorting:
                ascending = True

            if event.key == pygame.K_d and not sorting:
                ascending = False

    pygame.quit()


if __name__ == "__main__":
    main()
