function getUploadDate() {
    let button = document.getElementById("uploadAnswer")
    if (button.style.display === "none") {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
}
