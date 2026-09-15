# Model-View-Controller (MVC)

Separate the domain **Model**, the presentation **View**, and the input-handling
**Controller**.

- **Model:** data + business rules; notifies views of changes.
- **View:** renders the model; may observe it.
- **Controller:** translates user input into model operations and selects a view.

## Flow

```
user -> controller -> model -> (notify) -> view
```

## Trade-offs

- Clear separation and testable controllers.
- Controllers can become bloated ("fat controller").
- Server-side MVC (Rails, Django) vs client-side (backbone-style).

Related: MVP, MVVM, Presentation Model.
