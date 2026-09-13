package main

import (
	"fmt"
	"sync"
)

type Envelope struct {
	Type    string
	Payload int
	ReplyTo chan int
}

type CounterActor struct {
	mailbox chan Envelope
	state   int
	stop    chan struct{}
}

func NewCounterActor(bufferSize int) *CounterActor {
	a := &CounterActor{
		mailbox: make(chan Envelope, bufferSize),
		state:   0,
		stop:    make(chan struct{}),
	}
	go a.eventLoop()
	return a
}

func (a *CounterActor) eventLoop() {
	for {
		select {
		case msg := <-a.mailbox:
			switch msg.Type {
			case "INCREMENT":
				a.state += msg.Payload
			case "GET":
				if msg.ReplyTo != nil {
					msg.ReplyTo <- a.state
				}
			}
		case <-a.stop:
			return
		}
	}
}

func (a *CounterActor) Tell(msgType string, payload int) {
	a.mailbox <- Envelope{Type: msgType, Payload: payload}
}

func (a *CounterActor) Ask(msgType string) int {
	reply := make(chan int, 1)
	a.mailbox <- Envelope{Type: msgType, ReplyTo: reply}
	return <-reply
}

func (a *CounterActor) Stop() {
	close(a.stop)
}

func main() {
	actor := NewCounterActor(100)
	var wg sync.WaitGroup

	// Launch 10 concurrent producers each sending 10 increments
	numGoroutines := 10
	incrementsPerWorker := 10

	for i := 0; i < numGoroutines; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for j := 0; j < incrementsPerWorker; j++ {
				actor.Tell("INCREMENT", 1)
			}
		}()
	}

	wg.Wait()
	finalCount := actor.Ask("GET")
	expected := numGoroutines * incrementsPerWorker

	if finalCount != expected {
		panic(fmt.Sprintf("Expected %d, got %d", expected, finalCount))
	}

	actor.Stop()
	fmt.Printf("[Go Concurrency] Actor Model Mailbox verified: %d processed.\n", finalCount)
}
