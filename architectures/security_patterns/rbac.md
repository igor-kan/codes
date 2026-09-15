# Role-Based Access Control (RBAC)

Assign permissions to **roles**, and roles to subjects.

```
user -> role -> permission -> resource
```

## Benefits

- Simple to reason about and audit.
- Central administration; least privilege via tight roles.

## Challenges

- Role explosion as the system grows.
- Coarse for fine-grained, context-dependent rules.

Related: ABAC, Least Privilege.
