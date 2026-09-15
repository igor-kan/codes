// LRU cache using container/list and a map.
package main

import (
	"container/list"
	"fmt"
)

type entry struct{ key, value int }

type lruCache struct {
	capacity int
	items    *list.List
	index    map[int]*list.Element
}

func newLru(capacity int) *lruCache {
	return &lruCache{capacity: capacity, items: list.New(), index: map[int]*list.Element{}}
}

func (c *lruCache) get(key int) int {
	if element, ok := c.index[key]; ok {
		c.items.MoveToFront(element)
		return element.Value.(entry).value
	}
	return -1
}

func (c *lruCache) put(key, value int) {
	if element, ok := c.index[key]; ok {
		element.Value = entry{key, value}
		c.items.MoveToFront(element)
		return
	}
	if c.items.Len() == c.capacity {
		back := c.items.Back()
		delete(c.index, back.Value.(entry).key)
		c.items.Remove(back)
	}
	c.index[key] = c.items.PushFront(entry{key, value})
}

func main() {
	cache := newLru(2)
	cache.put(1, 1)
	cache.put(2, 2)
	if cache.get(1) != 1 {
		panic("expected 1")
	}
	cache.put(3, 3)
	if cache.get(2) != -1 {
		panic("expected eviction")
	}
	fmt.Println("lru cache ok")
}
