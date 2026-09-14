// Destructuring, spread/rest and optional chaining.
const user = { id: 7, name: "Ada", address: { city: "London" } };

const { id, name, address: { city } = {} } = user;
const [first, ...rest] = [10, 20, 30, 40];
const merged = { ...user, active: true };
const safeCity = user?.address?.city ?? "unknown";

export function summarize(...values) {
  return `first=${first} rest=${rest.length} max=${Math.max(id, ...values)} city=${city} ${safeCity}`;
}

export { merged, name };
