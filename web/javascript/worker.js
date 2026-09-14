// worker.js -- runs off the main thread.
self.onmessage = (event) => {
  const { limit } = event.data;
  let sum = 0;
  for (let i = 1; i <= limit; i += 1) sum += i;
  self.postMessage({ result: sum });
};
