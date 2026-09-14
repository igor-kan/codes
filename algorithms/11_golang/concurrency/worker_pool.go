package concurrency

import "sync"

type Task struct {
	ID int
	Process func() error
}

func WorkerPool(workers int, tasks <-chan Task, results chan<- error) {
	var wg sync.WaitGroup
	for i := 0; i < workers; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for task := range tasks {
				results <- task.Process()
			}
		}()
	}
	wg.Wait()
	close(results)
}
