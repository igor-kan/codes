# Model-View-Presenter (MVP)

The **Presenter** contains presentation logic and manipulates a passive **View**
through an interface; the **Model** holds domain state.

- View is dumb: exposes setters and events only.
- Presenter talks to the model and updates the view.
- Two styles: *passive view* and *supervising controller*.

## Benefits

- View is fully mockable; presenter is unit-testable without UI.
- Common in legacy desktop/web (GWT, WinForms).

Related: MVC, MVVM, Humble Object.
