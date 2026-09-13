/**
 * Gang of Four: Observer Behavioral Pattern in Java.
 * Demonstrates thread-safe publisher-subscriber state synchronization.
 */

import java.util.ArrayList;
import java.util.List;

interface Observer {
    void update(String event);
}

class Subject {
    private final List<Observer> observers = new ArrayList<>();
    private String state;

    public synchronized void attach(Observer observer) {
        observers.add(observer);
    }

    public synchronized void detach(Observer observer) {
        observers.remove(observer);
    }

    public synchronized void setState(String state) {
        this.state = state;
        notifyObservers();
    }

    public synchronized String getState() {
        return state;
    }

    private void notifyObservers() {
        for (Observer o : observers) {
            o.update(state);
        }
    }
}

class ConcreteObserver implements Observer {
    private final String name;
    private String lastEvent;

    public ConcreteObserver(String name) {
        this.name = name;
    }

    @Override
    public void update(String event) {
        this.lastEvent = event;
    }

    public String getLastEvent() {
        return lastEvent;
    }
}

public class ObserverPattern {
    public static void main(String[] args) {
        Subject subject = new Subject();
        ConcreteObserver obs1 = new ConcreteObserver("Observer-1");
        ConcreteObserver obs2 = new ConcreteObserver("Observer-2");

        subject.attach(obs1);
        subject.attach(obs2);

        subject.setState("EVENT_TRIGGERED_A");
        assert "EVENT_TRIGGERED_A".equals(obs1.getLastEvent());
        assert "EVENT_TRIGGERED_A".equals(obs2.getLastEvent());

        System.out.println("[Java Patterns] Observer state broadcast verified.");
    }
}
