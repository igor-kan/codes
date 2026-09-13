// Package main implements a concurrent worker pool with channel throttling and context cancellation.
// 
// Why Go for this module?
// Go's CSP concurrency model (goroutines, channels, and select statement) provides
// the gold standard for high-throughput cloud microservices (Kubernetes, Docker).
package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

type Task struct {
	ID   int
	Data string
}

type Result struct {
	TaskID int
	Output string
	Err    error
}

func Worker(ctx context.Context, id int, tasks <-chan Task, results chan<- Result, wg *sync.WaitGroup) {
	defer wg.Done()
	for {
		select {
		case <-ctx.Done():
			return
		case task, ok := <-tasks:
			if !ok {
				return
			}
			// Process task
			res := Result{
				TaskID: task.ID,
				Output: fmt.Sprintf("Worker %d processed %s", id, task.Data),
			}
			results <- res
		}
	}
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	numWorkers := 3
	numTasks := 10
	tasks := make(chan Task, numTasks)
	results := make(chan Result, numTasks)

	var wg sync.WaitGroup
	for w := 1; w <= numWorkers; w++ {
		wg.Add(1)
		go Worker(ctx, w, tasks, results, &wg)
	}

	for j := 1; j <= numTasks; j++ {
		tasks <- Task{ID: j, Data: fmt.Sprintf("Payload_%d", j)}
	}
	close(tasks)

	wg.Wait()
	close(results)

	for res := range results {
		fmt.Println(res.Output)
	}
}
