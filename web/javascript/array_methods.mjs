// Functional array processing.
const people = [
  { name: "Ada", age: 36 },
  { name: "Grace", age: 45 },
  { name: "Alan", age: 41 },
];

export const names = people.map((person) => person.name);
export const adults = people.filter((person) => person.age >= 40);
export const totalAge = people.reduce((sum, person) => sum + person.age, 0);
export const byAge = Object.groupBy(people, (p) => (p.age >= 40 ? "senior" : "junior"));
export const youngest = people.toSorted((a, b) => a.age - b.age)[0];
