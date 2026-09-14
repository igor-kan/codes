// A minimal function component.
export function Greeting({ name }) {
  return (
    <section>
      <h1>Hello, {name}!</h1>
      <p>Rendered by a React function component.</p>
    </section>
  );
}

export default function App() {
  return <Greeting name="world" />;
}
