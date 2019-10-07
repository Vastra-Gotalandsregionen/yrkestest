function checkLoaded() {
    return document.readyState === "complete";
}

function spin() {
    if(checkLoaded() == true) {

        setInterval(() => {
            document.querySelector('#arcs').style.display = "none";
        }, 2000);
    }
}