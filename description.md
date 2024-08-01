# SortVisualization: Visualize Different Sorting Algorithms with Custom Datasets

## Dependencies:
* [pygame: used to create visualization GUI](https://www.pygame.org/news)

## Quick Start:
**This visualizer is best used with integer values**
1. Import SortVisualization:
	`import  SortVisualization`

2. Create your custom list of integers:
    `import  random`
	`arr  =  list(random.randint(-100,  100) for  _  in  range(30))`

3. Visualize it!
	`SortVisualization.visualizeSort(arr)`

## All Methods:
* ` visualizeSort(arr)`
	* Visualizes All Sorting Algorithms with given list
* `visualizeRandomList(sizeOfArr, minValue, maxValue)`
	* Visualizes a random list with given size, minimum value, and maximum value
* ` visualizeBubbleSort(arr)`
	* Visualizes Bubble Sort with given list
* ` visualizeBogoSort(arr)`
	* Visualizes Bogo Sort with given list
* ` visualizeInsertionSort(arr)`
	* Visualizes Insertion Sort with given list
* ` visualizeCountingSort(arr)`
	* Visualizes Counting Sort with given list
* ` visualizeMiracleSort(arr)`
	* Visualizes Miracle Sort with given list
* ` visualizeSelectionSort(arr)`
	* Visualizes Selection Sort with given list
* ` visualizeShellSort(arr)`
	* Visualizes Shell Sort with given list