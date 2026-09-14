// Event delegation with a single listener.
export function attachListDelegation(list) {
  list.addEventListener("click", (event) => {
    const item = event.target.closest("li[data-id]");
    if (!item || !list.contains(item)) return;
    list.dispatchEvent(
      new CustomEvent("item:selected", {
        bubbles: true,
        detail: { id: item.dataset.id },
      }),
    );
  });
}
