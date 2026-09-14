// Classes, private fields and static members.
export class Shape {
  #name;
  constructor(name) {
    this.#name = name;
  }
  get name() {
    return this.#name;
  }
  area() {
    throw new Error("not implemented");
  }
  static describe(shape) {
    return `${shape.name}: ${shape.area().toFixed(2)}`;
  }
}

export class Circle extends Shape {
  #radius;
  constructor(radius) {
    super("circle");
    this.#radius = radius;
  }
  area() {
    return Math.PI * this.#radius ** 2;
  }
}
