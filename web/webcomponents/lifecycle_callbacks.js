// Lifecycle callbacks and attribute reflection.
class LiveClock extends HTMLElement {
  static get observedAttributes() { return ["paused"]; }

  connectedCallback() {
    this.timer = setInterval(() => this.#tick(), 1000);
    this.#tick();
  }
  disconnectedCallback() {
    clearInterval(this.timer);
  }
  attributeChangedCallback(name, oldValue, newValue) {
    if (name === "paused") this.paused = newValue !== null;
  }
  #tick() {
    if (!this.paused) this.textContent = new Date().toLocaleTimeString();
  }
}
customElements.define("live-clock", LiveClock);
