function getUploadDate() {

    let random = Math.floor(Math.random() * 26);
    const correctNumber = 14;
    let button = document.getElementById("uploadAnswer");
    let secret = document.getElementById("uploadSecret")

    if (button.style.display === "none") {
        button.style.display = "block";

    } else {
        button.style.display = "none";
        secret.style.display = "none";
    }
}
