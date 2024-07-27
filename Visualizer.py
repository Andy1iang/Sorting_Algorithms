# importing sorting algorithms
from BubbleSort import BubbleSort
from BogoSort import BogoSort
from InsertionSort import InsertionSort
from CountingSort import CountingSort
from MiracleSort import MiracleSort
from SelectionSort import SelectionSort
from ShellSort import ShellSort

# importing pygame & other libraries
import pygame
import random
import math

# initializing pygame
pygame.init()

# class storing screen display information
class ScreenInfo:

    # color codes
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    GREY = (128, 128, 128)
    LIGHT_GREY = (158, 155, 156)
    DARK_GREY = (98, 98, 98)
    BACKGROUND_COLOR = WHITE

    # paddings 
    SIDE_PADDING = 100
    TOP_PADDING = 100

    # offset to make smaller elements appear on screen
    BAR_OFFSET = 10

    # font selection and sizing
    TITLE_FONT = pygame.font.SysFont('Monocraft', 30)
    FONT = pygame.font.SysFont('Monocraft', 20)

    # initializing window
    def __init__(self, width, height, arr):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption("Sorting Visualizer")
        self.adjustBars(arr)

    # calculating bar height
    def adjustBars(self, arr):
        self.arr = arr
        self.minVal = min(arr)
        self.maxVal = max(arr)
        self.barWidth = math.floor((self.width - self.SIDE_PADDING) / len(arr))
        self.barHeight = math.floor(
            (self.height-self.TOP_PADDING)/(self.maxVal - self.minVal+1))
        self.startX = self.SIDE_PADDING // 2

# generating a new list to be sorted
def generateList(n, minVal, maxVal):
    return [random.randint(minVal, maxVal) for _ in range(n)]

# drawing the sorting screen
def draw(screen):

    # setting background color
    screen.window.fill(screen.BACKGROUND_COLOR)

    # loading texts
    title = screen.TITLE_FONT.render(
        "Sorting Visualizer", 1, screen.BLACK)
    controls = screen.FONT.render(
        "R: Reset | Space: Sort | A: Ascending | D: Descending", 1, screen.BLACK)
    
    # displaying texts to screen
    screen.window.blit(
        title, (screen.width//2 - title.get_width()//2, 5))
    
    screen.window.blit(
        controls, (screen.width//2 - controls.get_width()//2, 35))

    # drawing the sorting bars
    drawBars(screen)

    pygame.display.update()

# drawing the bars on the screen
def drawBars(screen, colorPositions={}, clear=False):

    # colors of the bars
    colors = [screen.LIGHT_GREY, screen.GREY, screen.DARK_GREY]

    # temporary array
    arr = screen.arr

    # if we are only redrawing the bars (when sorting)
    # we clear the bars first
    if clear:
        clearRect = (screen.SIDE_PADDING//2, screen.TOP_PADDING-screen.BAR_OFFSET, screen.width -
                     screen.SIDE_PADDING, screen.height - screen.TOP_PADDING)
        pygame.draw.rect(screen.window, screen.BACKGROUND_COLOR, clearRect)

    # drawing the bars on the screen
    for i, val in enumerate(arr):

        x = screen.startX + i * screen.barWidth
        y = screen.height - ((val - screen.minVal) * screen.barHeight) - screen.BAR_OFFSET

        # highlighting the ones we are switching
        color = colors[i % 3]
        if i in colorPositions:
            color = colorPositions[i]

        
        pygame.draw.rect(screen.window, color,
                         (x, y, screen.barWidth, screen.height))

    # redisplay if we are sorting
    if clear:
        pygame.display.update()


def main():

    # while-loop variable
    run = True
    clock = pygame.time.Clock()
    ascending = True
    sorting = False

    # instantiating screen and sorter
    screen = ScreenInfo(800, 600, generateList(50, 0, 100))
    sorter = ShellSort
    inst = sorter(screen.arr, ascending)
    sorterGen = None

    # updating screen
    draw(screen)

    while run:
        clock.tick(30)  # 60 fps

        if sorting:

            # if sorting is unfinished
            try:
                # get the possible indices to highlight
                result = next(sorterGen)

                # if we have indices to highlight
                if result:
                    one, two = result
                    drawBars(screen, {one: screen.GREEN, two: screen.RED}, True)

                else:
                    draw(screen)

            # when sorting is done
            except StopIteration:
                sorting = False
                draw(screen)

        # when events are triggered
        for event in pygame.event.get():

            # when quit is pressed
            if event.type == pygame.QUIT:
                run = False
                sorting = False

            # if no key is pressed, when move on to the next tick
            elif event.type != pygame.KEYDOWN:
                continue

            # resetting bars and screen & stops sorting
            elif event.key == pygame.K_r:
                screen = ScreenInfo(800, 600, generateList(50, 0, 100))
                inst = sorter(screen.arr, ascending)
                draw(screen)
                sorting = False

            # start sorting
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorterGen = inst.sort()

            elif event.key == pygame.K_a and not sorting:
                inst.ascending = True
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                inst.ascending = False
                ascending = False

    # quit game when loop is over (when quit is pressed)
    pygame.quit()


if __name__ == "__main__":
    main()
