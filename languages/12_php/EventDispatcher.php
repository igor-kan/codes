<?php
/**
 * PSR-14 Compliant Event Dispatcher.
 * 
 * Why PHP for this module?
 * Modern PHP (PHP 8.2+) powers the vast majority of web CMS and enterprise frameworks (Symfony, Laravel),
 * where event-driven decoupling is the foundational architecture.
 */

declare(strict_types=1);

interface StoppableEventInterface {
    public function isPropagationStopped(): bool;
}

class EventDispatcher {
    /** @var array<string, array<int, list<callable>>> */
    private array $listeners = [];

    public function addListener(string $eventName, callable $listener, int $priority = 0): void {
        $this->listeners[$eventName][$priority][] = $listener;
    }

    public function dispatch(object $event): object {
        $eventName = get_class($event);
        if (!isset($this->listeners[$eventName])) {
            return $event;
        }

        // Sort descending by priority
        krsort($this->listeners[$eventName]);

        foreach ($this->listeners[$eventName] as $priorityGroup) {
            foreach ($priorityGroup as $listener) {
                if ($event instanceof StoppableEventInterface && $event->isPropagationStopped()) {
                    break 2;
                }
                $listener($event);
            }
        }
        return $event;
    }
}
