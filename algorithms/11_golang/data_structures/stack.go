package data_structures
type Stack[T any] struct { data []T }
func (s *Stack[T]) Push(v T) { s.data=append(s.data,v) }
func (s *Stack[T]) Pop() T { n:=len(s.data)-1; v:=s.data[n]; s.data=s.data[:n]; return v }
func (s *Stack[T]) Peek() T { return s.data[len(s.data)-1] }
func (s *Stack[T]) Empty() bool { return len(s.data)==0 }