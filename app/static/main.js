function snurra() {
    var el = document.getElementById('arcs');
    var number = 5;
    var inter = 100;
    var loaderInterval = setInterval(() => {
        el.style.transform = "rotate("+number+"deg)";
        number = number+5;
        inter = inter + 100;
       if(inter == 2000) {
           document.querySelector('.result-container').style.display = "block";
            el.style.display = 'none';
            clearInterval(loaderInterval);
        }
    }, 100);
};