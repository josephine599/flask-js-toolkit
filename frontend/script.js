function getMessage() {
  fetch("http://127.0.0.1:5000/api/message")
    .then(response => response.json())
    .then(data => {
      document.getElementById("output").innerText = data.message;
    })
    .catch(error => console.error("Error:", error));
}
