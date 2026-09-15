# Attribute-Based Access Control (ABAC)

Authorization decisions from attributes of subject, resource, action, and
environment, evaluated by policy.

```rego
allow {
  input.subject.department == input.resource.department
  input.action == "read"
  input.environment.hour >= 9
}
```

## Benefits

- Fine-grained and context-aware (time, location, device).
- Policies externalized and testable (OPA/Rego, Cedar).

## Challenges

- Complexity, policy testing, and auditability.
- Performance of policy evaluation; caching.

Related: RBAC, Zero Trust, Policy as Code.
