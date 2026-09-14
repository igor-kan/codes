// Persisting typed state in localStorage.
const KEY = "app.settings";

export function loadSettings(defaults) {
  try {
    const raw = localStorage.getItem(KEY);
    return raw ? { ...defaults, ...JSON.parse(raw) } : { ...defaults };
  } catch {
    return { ...defaults };
  }
}

export function saveSettings(settings) {
  localStorage.setItem(KEY, JSON.stringify(settings));
}

export function clearSettings() {
  localStorage.removeItem(KEY);
}
