# Model-View-ViewModel (MVVM)

The **ViewModel** exposes data and commands as observable properties; the
**View** binds to them declaratively, so no code-behind logic is needed.

```
View <--binding--> ViewModel <--> Model
```

- Two-way binding keeps view and view model in sync.
- Commands replace event handlers.
- Popular in WPF, SwiftUI, Vue, Svelte, Angular (as components + services).

## Trade-offs

- Great for form-heavy UIs and designer/developer separation.
- Two-way binding can hide control flow and hurt debuggability at scale.

Related: MVP, Presentation Model, Redux.
