package graphs

func TarjanSCC(graph map[int][]int) [][]int {
	var index, lowlink map[int]int
	var indexCounter int
	var stack []int
	var onStack map[int]bool
	var sccs [][]int

	index = make(map[int]int)
	lowlink = make(map[int]int)
	onStack = make(map[int]bool)

	var strongconnect func(int)
	strongconnect = func(v int) {
		index[v] = indexCounter
		lowlink[v] = indexCounter
		indexCounter++
		stack = append(stack, v)
		onStack[v] = true

		for _, w := range graph[v] {
			if _, ok := index[w]; !ok {
				strongconnect(w)
				if lowlink[w] < lowlink[v] {
					lowlink[v] = lowlink[w]
				}
			} else if onStack[w] {
				if index[w] < lowlink[v] {
					lowlink[v] = index[w]
				}
			}
		}

		if lowlink[v] == index[v] {
			var scc []int
			for {
				w := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				onStack[w] = false
				scc = append(scc, w)
				if w == v {
					break
				}
			}
			sccs = append(sccs, scc)
		}
	}

	for v := range graph {
		if _, ok := index[v]; !ok {
			strongconnect(v)
		}
	}
	return sccs
}
