const output = document.getElementById("output");
const button = document.getElementById("fetch-btn");

function getMessage() {
  fetch("/api/message")
    .then(res => res.json())
    .then(data => {
      output.innerText = data.message;
      output.classList.add("show");
      setTimeout(() => output.classList.remove("show"), 1200);
    })
    .catch(err => console.error("Error:", err));
}

button.addEventListener("click", getMessage);