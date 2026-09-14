// Managing complex state with useReducer.
import { useReducer } from "react";

const initialState = { todos: [], filter: "all" };

function reducer(state, action) {
  switch (action.type) {
    case "add":
      return { ...state, todos: [...state.todos, { id: Date.now(), text: action.text, done: false }] };
    case "toggle":
      return { ...state, todos: state.todos.map((t) => (t.id === action.id ? { ...t, done: !t.done } : t)) };
    case "filter":
      return { ...state, filter: action.value };
    default:
      throw new Error(`Unknown action: ${action.type}`);
  }
}

export function TodoList() {
  const [state, dispatch] = useReducer(reducer, initialState);
  const visible = state.todos.filter((t) => state.filter === "all" || t.done === (state.filter === "done"));
  return (
    <ul>
      {visible.map((t) => (
        <li key={t.id} onClick={() => dispatch({ type: "toggle", id: t.id })}>
          {t.done ? "✓" : "○"} {t.text}
        </li>
      ))}
    </ul>
  );
}
