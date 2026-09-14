// Fetch with error handling and JSON parsing.
export async function getUser(id) {
  const response = await fetch(`/api/users/${id}`, {
    headers: { Accept: "application/json" },
  });
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return response.json();
}

export async function createUser(payload) {
  const response = await fetch("/api/users", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return response.json();
}
