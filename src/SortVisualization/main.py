import copy
import math
import random
import pygame
import os
import sys

# importing sorting algorithms
sys.path.append(os.path.dirname(__file__))
from ShellSort import ShellSort
from SelectionSort import SelectionSort
from MiracleSort import MiracleSort
from CountingSort import CountingSort
from InsertionSort import InsertionSort
from BogoSort import BogoSort
from BubbleSort import BubbleSort

# initializing pygame
pygame.init()


class ScreenInfo:
    # class storing screen display information

    # color codes
    BLACK = (22, 22, 29)
    WHITE = (245, 245, 240)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    GREY = (128, 128, 128)
    LIGHT_GREY = (158, 155, 156)
    DARK_GREY = (98, 98, 98)
    BACKGROUND_COLOR = WHITE

    # paddings
    SIDE_PADDING_RATIO = 0.125
    TOP_PADDING_RATIO = 0.175

    # offset to make smaller elements appear on screen
    BAR_OFFSET_RATIO = 0.02

    # font sizing
    TITLE_FONT_RATIO = 0.05
    FONT_RATIO = 0.025
    SORTERS = {
        "Bubble Sort": BubbleSort,
        "Bogo Sort": BogoSort,
        "Insertion Sort": InsertionSort,
        "Counting Sort": CountingSort,
        "Miracle Sort": MiracleSort,
        "Selection Sort": SelectionSort,
        "Shell Sort": ShellSort,
    }

    SORT_SELECTIONS = [
        "Bubble Sort",
        "Bogo Sort",
        "Insertion Sort",
        "Counting Sort",
        "Miracle Sort",
        "Selection Sort",
        "Shell Sort",
    ]

    # initializing window
    def __init__(self, width, height, arr, sorterIdx):

        # screen information
        self.width = width
        self.height = height
        self.sidePadding = math.floor(
            self.width * self.SIDE_PADDING_RATIO
        )  # side padding for bars
        self.topPadding = math.floor(
            self.height * self.TOP_PADDING_RATIO
        )  # top padding for bars
        # extra visibility for bars
        self.barOffset = math.floor(self.height * self.BAR_OFFSET_RATIO)

        self.sorterIdx = sorterIdx

        # updating font size and selection
        self.titleFont = pygame.font.SysFont(
            "Courier", math.floor(self.height * self.TITLE_FONT_RATIO)
        )
        self.font = pygame.font.SysFont(
            "Courier", math.floor(self.height * self.FONT_RATIO)
        )

        # initializing window
        self.window = pygame.display.set_mode(
            (self.width, self.height), pygame.RESIZABLE
        )
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
            (self.height - self.topPadding) / (self.maxVal - self.minVal + 1)
        )
        self.startX = self.sidePadding // 2


class Button:
    def __init__(self, screen, x, y, width, height, image=None, text=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.text = text

    def update(self):
        self.surface = pygame.image.load(self.image)
        self.surface = pygame.transform.smoothscale(
            self.surface, (self.width, self.height)
        )
        self.screen.window.blit(self.surface, (self.x, self.y))


def generateList(n, minVal, maxVal):
    # generating a new list to be sorted
    return [random.randint(minVal, maxVal) for _ in range(n)]


def draw(screen, darkMode, ascending):
    # drawing the sorting screen

    # setting background color
    screen.window.fill(screen.BACKGROUND_COLOR)

    # loading texts
    if darkMode:
        title = screen.titleFont.render(
            screen.SORT_SELECTIONS[screen.sorterIdx], True, screen.WHITE
        )
        controls = screen.font.render(
            "R: Reset | Space: Sort | A: Ascending | D: Descending", True, screen.WHITE
        )
        direction = screen.font.render(
            "Ascending Order" if ascending else "Descending Order", True, screen.WHITE
        )

    else:
        title = screen.titleFont.render(
            screen.SORT_SELECTIONS[screen.sorterIdx], True, screen.BLACK
        )
        controls = screen.font.render(
            "R: Reset | Space: Sort | A: Ascending | D: Descending", True, screen.BLACK
        )
        direction = screen.font.render(
            "Ascending Order" if ascending else "Descending Order", True, screen.BLACK
        )

    # displaying texts to screen
    screen.window.blit(title, (screen.width // 2 - title.get_width() // 2, 10))

    screen.window.blit(
        controls,
        (screen.width // 2 - controls.get_width() // 2, title.get_rect().height + 15),
    )

    screen.window.blit(
        direction,
        (
            screen.width // 2 - direction.get_width() // 2,
            title.get_rect().height + controls.get_rect().height + 20,
        ),
    )

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
        clearRect = (
            screen.sidePadding // 2,
            screen.topPadding - screen.barOffset,
            screen.width - screen.sidePadding,
            screen.height - screen.topPadding,
        )
        pygame.draw.rect(screen.window, screen.BACKGROUND_COLOR, clearRect)

    # drawing the bars on the screen
    for i, val in enumerate(arr):

        x = screen.startX + i * screen.barWidth
        y = (
            screen.height - ((val - screen.minVal) * screen.barHeight)
        ) - screen.barOffset  # ?????

        # highlighting the ones we are switching
        color = colors[i % 3]
        if i in colorPositions:
            color = colorPositions[i]

        pygame.draw.rect(screen.window, color, (x, y, screen.barWidth, screen.height))

    # redisplay if we are sorting
    if clear:
        pygame.display.update()


def finalCheck(screen, ascending):
    # checking if the array is sorted
    for i in range(len(screen.arr) - 1):
        if (ascending and screen.arr[i] > screen.arr[i + 1]) or (
            not ascending and screen.arr[i] < screen.arr[i + 1]
        ):
            return False
        else:
            yield i, i + 1
    return True


def drawMoon(screen, moon, darkMode):
    sizing = math.floor(screen.width * 0.025)
    moon.x = screen.width - 50
    moon.y = 20
    moon.width = sizing
    moon.height = sizing

    if darkMode:
        moon.image = os.path.dirname(__file__) + "/light_moon.png"
    else:
        moon.image = os.path.dirname(__file__) + "/dark_moon.png"

    moon.update()
    pygame.display.update()


def drawArrows(screen, left, right, darkMode):
    sizing = math.floor(screen.height * screen.FONT_RATIO)
    left.x = screen.width * 0.3
    right.x = screen.width * 0.7
    left.y = 20
    right.y = 20
    left.width = sizing
    left.height = sizing
    right.width = sizing
    right.height = sizing
    pygame.draw.polygon(
        screen.window,
        screen.WHITE if darkMode else screen.BLACK,
        (
            (left.x - sizing, left.y + (sizing // 2)),
            (left.x, left.y),
            (left.x, left.y + sizing),
        ),
    )
    pygame.draw.polygon(
        screen.window,
        screen.WHITE if darkMode else screen.BLACK,
        (
            (right.x, right.y),
            (right.x + sizing, right.y + (sizing // 2)),
            (right.x, right.y + sizing),
        ),
    )
    pygame.display.update()


def darkModeDisplay(screen, moon, left, right, darkMode, ascending):
    if darkMode:
        screen.BACKGROUND_COLOR = screen.BLACK

    else:
        screen.BACKGROUND_COLOR = screen.WHITE

    draw(screen, darkMode, ascending)
    drawMoon(screen, moon, darkMode)
    drawArrows(screen, left, right, darkMode)


def main(arr, sorterIdx=0):

    for i in arr:
        if type(i) != int:
            raise Exception("All elements must be integers")

    restoreArr = copy.deepcopy(arr)

    # while-loop variable
    run = True
    clock = pygame.time.Clock()
    ascending = True
    sorting = False
    darkMode = False
    checked = False

    # instantiating screen and sorter
    screen = ScreenInfo(1280, 800, copy.deepcopy(restoreArr), sorterIdx)
    sorter = screen.SORTERS[screen.SORT_SELECTIONS[screen.sorterIdx]]
    inst = sorter(screen.arr, ascending)
    sorterGen = None

    # instantiating buttons
    moon = Button(screen, 0, 0, 0, 0, os.path.dirname(__file__) + "/dark_moon.png")
    leftArrow = Button(
        screen,
        0,
        0,
        0,
        0,
    )
    rightArrow = Button(
        screen,
        0,
        0,
        0,
        0,
    )

    # updating screen
    draw(screen, darkMode, ascending)
    drawMoon(screen, moon, darkMode)
    drawArrows(screen, leftArrow, rightArrow, darkMode)

    while run:
        clock.tick(60)  # 60 fps

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
                    # draw(screen, darkMode, ascending)
                    # drawMoon(screen, moon, darkMode)
                    drawBars(screen, {}, True)

            # when sorting is done
            except StopIteration:
                # screen.restoreArr = copy.deepcopy(screen.arr)
                if not checked:
                    checker = finalCheck(screen, ascending)
                    checked = True
                try:
                    result = next(checker)
                    if not result:
                        # show that sorter is broken
                        sorting = False
                    else:
                        one, two = result
                        drawBars(screen, {one: screen.GREEN, two: screen.RED}, True)
                except StopIteration:
                    sorting = False
                    checked = False
                    darkModeDisplay(
                        screen, moon, leftArrow, rightArrow, darkMode, ascending
                    )

        # when events are triggered
        for event in pygame.event.get():

            # when quit is pressed
            if event.type == pygame.QUIT:
                run = False
                sorting = False
                darkMode = False

            elif event.type == pygame.VIDEORESIZE:
                screen = ScreenInfo(
                    screen.window.get_width(),
                    screen.window.get_height(),
                    copy.deepcopy(screen.arr),
                    screen.sorterIdx,
                )
                inst = sorter(screen.arr, ascending)
                sorterGen = inst.sort()
                darkModeDisplay(
                    screen, moon, leftArrow, rightArrow, darkMode, ascending
                )

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if moon.surface.get_rect().move(moon.x, moon.y).collidepoint(event.pos):
                    darkMode = not darkMode
                    darkModeDisplay(
                        screen, moon, leftArrow, rightArrow, darkMode, ascending
                    )

                elif (
                    not sorting
                    and leftArrow.x - leftArrow.width <= event.pos[0] <= leftArrow.x
                    and leftArrow.y <= event.pos[1] <= leftArrow.y + leftArrow.height
                ):
                    screen.sorterIdx = (screen.sorterIdx - 1) % len(
                        screen.SORT_SELECTIONS
                    )
                    sorter = screen.SORTERS[screen.SORT_SELECTIONS[screen.sorterIdx]]
                    inst = sorter(screen.arr, ascending)
                    darkModeDisplay(
                        screen, moon, leftArrow, rightArrow, darkMode, ascending
                    )

                elif (
                    not sorting
                    and rightArrow.x <= event.pos[0] <= rightArrow.x + rightArrow.width
                    and rightArrow.y <= event.pos[1] <= rightArrow.y + rightArrow.height
                ):
                    screen.sorterIdx = (screen.sorterIdx + 1) % len(
                        screen.SORT_SELECTIONS
                    )
                    sorter = screen.SORTERS[screen.SORT_SELECTIONS[screen.sorterIdx]]
                    inst = sorter(screen.arr, ascending)
                    darkModeDisplay(
                        screen, moon, leftArrow, rightArrow, darkMode, ascending
                    )

            # if no key is pressed, when move on to the next tick
            elif event.type != pygame.KEYDOWN:
                continue

            # resetting bars and screen & stops sorting
            elif event.key == pygame.K_r:
                sorting = False
                screen = ScreenInfo(
                    screen.window.get_width(),
                    screen.window.get_height(),
                    copy.deepcopy(restoreArr),
                    screen.sorterIdx,
                )
                inst = sorter(screen.arr, ascending)
                sorterGen = inst.sort()
                darkModeDisplay(
                    screen, moon, leftArrow, rightArrow, darkMode, ascending
                )

            # start sorting
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorterGen = inst.sort()

            elif event.key == pygame.K_a and not sorting:
                inst.ascending = True
                ascending = True
                darkModeDisplay(
                    screen, moon, leftArrow, rightArrow, darkMode, ascending
                )

            elif event.key == pygame.K_d and not sorting:
                inst.ascending = False
                ascending = False
                darkModeDisplay(
                    screen, moon, leftArrow, rightArrow, darkMode, ascending
                )

            elif event.key == pygame.K_RIGHT and not sorting:
                screen.sorterIdx = (screen.sorterIdx + 1) % len(screen.SORT_SELECTIONS)
                sorter = screen.SORTERS[screen.SORT_SELECTIONS[screen.sorterIdx]]
                inst = sorter(screen.arr, ascending)
                darkModeDisplay(
                    screen, moon, leftArrow, rightArrow, darkMode, ascending
                )

            elif event.key == pygame.K_LEFT and not sorting:
                screen.sorterIdx = (screen.sorterIdx - 1) % len(screen.SORT_SELECTIONS)
                sorter = screen.SORTERS[screen.SORT_SELECTIONS[screen.sorterIdx]]
                inst = sorter(screen.arr, ascending)
                darkModeDisplay(
                    screen, moon, leftArrow, rightArrow, darkMode, ascending
                )

    # quit game when loop is over (when quit is pressed)
    pygame.quit()


def visualizeSort(arr):
    main(arr)


def visualizeRandomList(size, minVal=-500, maxVal=500):
    main(generateList(size, minVal, maxVal))


def visualizeBubbleSort(arr):
    main(arr, 0)


def visualizeBogoSort(arr):
    main(arr, 1)


def visualizeInsertionSort(arr):
    main(arr, 2)


def visualizeCountingSort(arr):
    main(arr, 3)


def visualizeMiracleSort(arr):
    main(arr, 4)


def visualizeSelectionSort(arr):
    main(arr, 5)


def visualizeShellSort(arr):
    main(arr, 6)


if __name__ == "__main__":
    main(generateList(50, 0, 100))
