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
import copy

# initializing pygame
pygame.init()

## TODO:
# Add final check to make sure array is sorted


class ScreenInfo:
    # class storing screen display information

    # color codes
    BLACK =  (22, 22, 29) 
    WHITE = (245, 245, 240)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    GREY = (128, 128, 128)
    LIGHT_GREY = (158, 155, 156)
    DARK_GREY = (98, 98, 98)
    BACKGROUND_COLOR = WHITE

    # paddings
    SIDE_PADDING_RATIO = 0.125
    TOP_PADDING_RATIO = 0.125

    # offset to make smaller elements appear on screen
    BAR_OFFSET_RATIO = 0.02

    # font sizing
    TITLE_FONT_RATIO = 0.035
    FONT_RATIO = 0.025

    # initializing window
    def __init__(self, width, height, arr):
        self.width = width
        self.height = height
        self.sidePadding = math.floor(self.width * self.SIDE_PADDING_RATIO)
        self.topPadding = math.floor(self.height * self.TOP_PADDING_RATIO)
        self.barOffset = math.floor(self.height * self.BAR_OFFSET_RATIO)

        # font selection
        self.titleFont = pygame.font.SysFont(
            'Courier', math.floor(self.height*self.TITLE_FONT_RATIO))
        self.font = pygame.font.SysFont(
            'Courier', math.floor(self.height*self.FONT_RATIO))

        self.window = pygame.display.set_mode(
            (self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("Sorting Visualizer")
        self.adjustBars(arr)

    # calculating bar height
    def adjustBars(self, arr):
        self.arr = arr
        self.restoreArr = copy.deepcopy(arr)
        self.minVal = min(arr)
        self.maxVal = max(arr)
        self.barWidth = math.floor((self.width - self.sidePadding) / len(arr))
        self.barHeight = math.floor(
            (self.height-self.topPadding)/(self.maxVal - self.minVal+1))
        self.startX = self.sidePadding // 2


class Button:
    def __init__(self, screen, x, y, width, height, image, text=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.surface = pygame.image.load(image)
        self.surface = pygame.transform.smoothscale(self.surface, (width, height))
        self.text = text
        self.update()
        
    def update(self):
        self.screen.window.blit(self.surface, (self.x, self.y))




def generateList(n, minVal, maxVal):
    # generating a new list to be sorted
    return [random.randint(minVal, maxVal) for _ in range(n)]


def draw(screen):
    # drawing the sorting screen

    # setting background color
    screen.window.fill(screen.BACKGROUND_COLOR)

    # loading texts
    title = screen.titleFont.render(
        "Sorting Visualizer", 1, screen.BLACK)
    controls = screen.font.render(
        "R: Reset | Space: Sort | A: Ascending | D: Descending", 1, screen.BLACK)

    # TODO:
    # Captions Locations Need to be Dynamically set

    # displaying texts to screen
    screen.window.blit(
        title, (screen.width//2 - title.get_width()//2, 5))

    screen.window.blit(
        controls, (screen.width//2 - controls.get_width()//2, 35))

    # drawing the sorting bars
    drawBars(screen)

    pygame.display.update()


def drawBars(screen, colorPositions={}, clear=False):
    # drawing the bars on the screen

    # colors of the bars
    colors = [screen.LIGHT_GREY, screen.GREY, screen.DARK_GREY]

    # temporary array
    arr = screen.arr

    # if we are only redrawing the bars (when sorting)
    # we clear the bars first
    if clear:
        clearRect = (screen.sidePadding//2, screen.topPadding-screen.barOffset, screen.width -
                     screen.sidePadding, screen.height - screen.topPadding)
        pygame.draw.rect(screen.window, screen.BACKGROUND_COLOR, clearRect)

    # drawing the bars on the screen
    for i, val in enumerate(arr):

        x = screen.startX + i * screen.barWidth
        y = (screen.height - ((val - screen.minVal)*screen.barHeight)) - \
            screen.barOffset  # ?????

        # highlighting the ones we are switching
        color = colors[i % 3]
        if i in colorPositions:
            color = colorPositions[i]

        pygame.draw.rect(screen.window, color,
                         (x, y, screen.barWidth, screen.height))

    # redisplay if we are sorting
    if clear:
        pygame.display.update()


def drawMoon(screen):
    sizing = math.floor(screen.width *0.025) 
    moon = Button(screen, screen.width-50, 20, sizing , sizing, "dark_moon.png")
    pygame.display.update()


def main():

    # while-loop variable
    run = True
    clock = pygame.time.Clock()
    ascending = True
    sorting = False

    # instantiating screen and sorter
    screen = ScreenInfo(1280, 800, generateList(50, 0, 100))
    sorter = SelectionSort
    inst = sorter(screen.arr, ascending)
    sorterGen = None

    # updating screen
    draw(screen)
    drawMoon(screen)

    while run:
        clock.tick(60)  # 60 fps

        if sorting:

            if sorter == MiracleSort:
                pass
                # add line to print divine intervention

            # if sorting is unfinished
            try:
                # get the possible indices to highlight
                result = next(sorterGen)

                # if we have indices to highlight
                if result:
                    one, two = result
                    drawBars(screen, {one: screen.GREEN,
                             two: screen.RED}, True)

                else:
                    draw(screen)
                    drawMoon(screen)

            # when sorting is done
            except StopIteration:
                screen.restoreArr = copy.deepcopy(screen.arr)
                sorting = False
                draw(screen)
                drawMoon(screen)

        # when events are triggered
        for event in pygame.event.get():

            # when quit is pressed
            if event.type == pygame.QUIT:
                run = False
                sorting = False

            elif event.type == pygame.VIDEORESIZE:
                # sorting = False
                screen = ScreenInfo(screen.window.get_width(
                ), screen.window.get_height(), copy.deepcopy(screen.arr))
                inst = sorter(screen.arr, ascending)
                sorterGen = inst.sort()
                draw(screen)
                drawMoon(screen)

            # if no key is pressed, when move on to the next tick
            elif event.type != pygame.KEYDOWN:
                continue

            # resetting bars and screen & stops sorting
            elif event.key == pygame.K_r:
                screen = ScreenInfo(
                    screen.width, screen.height, generateList(50, 0, 100))
                inst = sorter(screen.arr, ascending)
                draw(screen)
                drawMoon(screen)
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
