// Controlled form inputs with validation.
import { useState } from "react";

export function SignupForm({ onSubmit }) {
  const [form, setForm] = useState({ email: "", password: "" });
  const [error, setError] = useState("");

  function handleChange(event) {
    setForm({ ...form, [event.target.name]: event.target.value });
  }

  function handleSubmit(event) {
    event.preventDefault();
    if (form.password.length < 8) {
      setError("Password must be at least 8 characters.");
      return;
    }
    setError("");
    onSubmit(form);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="email" type="email" value={form.email} onChange={handleChange} required />
      <input name="password" type="password" value={form.password} onChange={handleChange} required />
      {error && <p role="alert">{error}</p>}
      <button type="submit">Create account</button>
    </form>
  );
}
