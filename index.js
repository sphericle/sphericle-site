function getUploadDate() {
    let random = 50;
    let button = document.getElementById("uploadAnswer");
    let secret = document.getElementById("uploadSecret")
    if (button.style.display === "none" && random !== 50) {
        button.style.display = "block";
        console.log(random);
    } else if (button.style.display === "none" && random === 50) {
        secret.style.display = "block"
    } else {
        button.style.display = "none";
        secret.style.display = "none";
    }
}
