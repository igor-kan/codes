package main

import (
	"container/heap"
	"fmt"
	"math"
)

type Point struct {
	r, c int
}

type Item struct {
	pt     Point
	fScore int
	gScore int
	index  int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int           { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].fScore < pq[j].fScore }
func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}
func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

func manhattan(a, b Point) int {
	return int(math.Abs(float64(a.r-b.r)) + math.Abs(float64(a.c-b.c)))
}

func aStarGrid(grid [][]int, start, goal Point) []Point {
	rows := len(grid)
	cols := len(grid[0])

	pq := make(PriorityQueue, 0)
	heap.Init(&pq)

	gScore := make(map[Point]int)
	cameFrom := make(map[Point]Point)

	gScore[start] = 0
	heap.Push(&pq, &Item{pt: start, fScore: manhattan(start, goal), gScore: 0})

	dirs := []Point{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	for pq.Len() > 0 {
		currItem := heap.Pop(&pq).(*Item)
		curr := currItem.pt

		if curr == goal {
			path := []Point{goal}
			c := goal
			for c != start {
				c = cameFrom[c]
				path = append(path, c)
			}
			// reverse
			for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
				path[i], path[j] = path[j], path[i]
			}
			return path
		}

		if currItem.gScore > gScore[curr] {
			continue
		}

		for _, d := range dirs {
			nr, nc := curr.r+d.r, curr.c+d.c
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 0 {
				neighbor := Point{nr, nc}
				tentativeG := currItem.gScore + 1
				prevG, exists := gScore[neighbor]
				if !exists || tentativeG < prevG {
					gScore[neighbor] = tentativeG
					cameFrom[neighbor] = curr
					heap.Push(&pq, &Item{
						pt:     neighbor,
						fScore: tentativeG + manhattan(neighbor, goal),
						gScore: tentativeG,
					})
				}
			}
		}
	}
	return nil
}

func main() {
	grid := [][]int{
		{0, 0, 0, 0, 0},
		{1, 1, 1, 1, 0},
		{0, 0, 0, 0, 0},
		{0, 1, 1, 1, 1},
		{0, 0, 0, 0, 0},
	}
	path := aStarGrid(grid, Point{0, 0}, Point{4, 4})
	if len(path) != 17 {
		panic(fmt.Sprintf("Expected 17 steps, got %d", len(path)))
	}
	fmt.Printf("[Go A*] Path computed successfully: %d steps.\n", len(path))
}
