// Clone a <template> for repeated rendering.
const template = document.createElement("template");
template.innerHTML = `
  <li class="row">
    <span class="name"></span>
    <span class="score"></span>
  </li>`;

function render(list, items) {
  const frag = document.createDocumentFragment();
  for (const item of items) {
    const node = template.content.cloneNode(true);
    node.querySelector(".name").textContent = item.name;
    node.querySelector(".score").textContent = String(item.score);
    frag.appendChild(node);
  }
  list.replaceChildren(frag);
}
