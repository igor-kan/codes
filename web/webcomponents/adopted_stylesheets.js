// Share one constructable stylesheet across many components.
const shared = new CSSStyleSheet();
shared.replaceSync(`
  :host { display: inline-block; }
  .chip { border-radius: 9999px; padding: .25rem .75rem; background: #e0f2fe; }`);

class TagChip extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" }).adoptedStyleSheets = [shared];
    this.shadowRoot.innerHTML =
      `<span class="chip">${this.getAttribute("label") ?? "tag"}</span>`;
  }
}
customElements.define("tag-chip", TagChip);
