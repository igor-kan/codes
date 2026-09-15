# Test Doubles

Stand-ins for collaborators: **dummy**, **stub**, **spy**, **mock**, **fake**.

| Double | Behaviour |
|:---|:---|
| Dummy | passed but never used |
| Stub | returns canned answers |
| Spy | records calls |
| Mock | asserts expectations |
| Fake | lightweight working implementation |

## Guidance

- Prefer fakes/hand-written doubles over heavy mocking frameworks.
- Mock at architectural boundaries, not internal details.
- Too many mocks signal tight coupling — refactor instead.

Related: Ports and Adapters, Test Pyramid.
