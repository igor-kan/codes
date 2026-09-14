// Define a custom element with a shadow root.
class CounterButton extends HTMLElement {
  connectedCallback() {
    this.count = 0;
    this.attachShadow({ mode: "open" });
    this.shadowRoot.innerHTML = `
      <style>button { font: inherit; padding: .25rem .75rem; }</style>
      <button type="button">clicked 0 times</button>`;
    this.shadowRoot.querySelector("button").addEventListener("click", () => {
      this.count += 1;
      this.shadowRoot.querySelector("button").textContent = `clicked ${this.count} times`;
    });
  }
}
customElements.define("counter-button", CounterButton);
