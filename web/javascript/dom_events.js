// DOM selection and event handling.
const button = document.querySelector("#save");
const output = document.querySelector("#output");

function handleClick(event) {
  event.preventDefault();
  output.textContent = `saved at ${new Date().toISOString()}`;
}

button.addEventListener("click", handleClick);
