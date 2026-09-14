// Encapsulated styles via the shadow DOM.
class FancyBox extends HTMLElement {
  constructor() {
    super();
    const root = this.attachShadow({ mode: "open" });
    const sheet = new CSSStyleSheet();
    sheet.replaceSync(`
      :host { display: block; border: 2px solid rebeccapurple; padding: 1rem; }
      ::slotted(h2) { margin: 0 0 .5rem; }`);
    root.adoptedStyleSheets = [sheet];
    root.innerHTML = "<h2><slot name='title'></slot></h2><slot></slot>";
  }
}
customElements.define("fancy-box", FancyBox);
