function getUploadDate() {
    random = Math.floor(Math.random() * 101);
    let button = document.getElementById("uploadAnswer");
    let secret = document.getElementById("uploadSecret")
    if (button.style.display === "none" && secret !== 50) {
        button.style.display = "block";
    } else if (button.style.display === "none" && secret === 50) {
        secret.style.display = "block"
    } else {
        button.style.display = "none";
        secret.style.display = "none";
    }
}
