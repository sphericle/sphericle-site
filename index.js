function getUploadDate() {
    let button = document.getElementById("uploadAnswer")
    if (button.style.display === "block") {
        button.style.display = "none";
    } else {
        button.style.display = "block";
    }
}
