function getUploadDate() {
    let random = Math.floor(Math.random() * 26);
    const correctNumber = 14
    let button = document.getElementById("uploadAnswer");
    let secret = document.getElementById("uploadSecret")
    if (button.style.display === "none" && random !== correctNumber) {
        button.style.display = "block";
        console.log(random);
    } else if (button.style.display === "none" && random === correctNumber) {
        secret.style.display = "block"
    } else {
        button.style.display = "none";
        secret.style.display = "none";
    }
}
