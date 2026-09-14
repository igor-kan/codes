package concurrency

type Message struct {
	Data    interface{}
	ReplyTo chan interface{}
}

type Actor struct {
	inbox chan Message
}

func NewActor(bufferSize int) *Actor {
	return &Actor{inbox: make(chan Message, bufferSize)}
}

func (a *Actor) Start(handler func(Message)) {
	go func() {
		for msg := range a.inbox {
			handler(msg)
		}
	}()
}

func (a *Actor) Send(msg Message) {
	a.inbox <- msg
}
