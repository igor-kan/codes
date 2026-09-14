// Offload heavy work to a Web Worker.
// main.js
export function startWorker(input) {
  const worker = new Worker(new URL("./worker.js", import.meta.url), { type: "module" });
  return new Promise((resolve, reject) => {
    worker.onmessage = (event) => {
      resolve(event.data);
      worker.terminate();
    };
    worker.onerror = reject;
    worker.postMessage(input);
  });
}
