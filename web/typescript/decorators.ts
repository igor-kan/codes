// Stage-3 decorators (requires "experimentalDecorators" off).
function logged<T extends (...args: never[]) => unknown>(
  target: unknown,
  context: ClassMethodDecoratorContext,
) {
  const name = String(context.name);
  return function replacement(this: unknown, ...args: never[]) {
    console.log(`[${name}] called with`, args);
    return (target as T).apply(this, args);
  };
}

export class Calculator {
  @logged
  add(a: number, b: number): number {
    return a + b;
  }
}
