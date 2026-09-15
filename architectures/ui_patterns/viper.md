# VIPER

Clean-architecture applied to iOS: **View**, **Interactor**, **Presenter**,
**Entity**, **Router**.

- **View:** displays content, forwards events.
- **Interactor:** business logic and use cases.
- **Presenter:** formats data for the view.
- **Entity:** plain domain models.
- **Router:** navigation/wireframe.

## Benefits

- Strong testability and separation of concerns for large apps.
- Each layer independently changeable.

Trade-offs: heavy boilerplate; overkill for small apps.

Related: MVC, Clean Architecture, MVP.
