// Data fetching with useEffect, cleanup and AbortController.
import { useEffect, useState } from "react";

export function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();
    setUser(null);
    setError(null);

    fetch(`/api/users/${userId}`, { signal: controller.signal })
      .then((res) => (res.ok ? res.json() : Promise.reject(new Error(String(res.status)))))
      .then(setUser)
      .catch((err) => {
        if (err.name !== "AbortError") setError(err);
      });

    return () => controller.abort();
  }, [userId]);

  if (error) return <p role="alert">{error.message}</p>;
  if (!user) return <p>Loading…</p>;
  return <h1>{user.name}</h1>;
}
