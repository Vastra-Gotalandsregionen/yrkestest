var arcs = document.querySelector('.arcs-div');

arcs.addEventListener( 'animationend', function( event ) { 
    document.querySelector('#arcs').style.display = 'none';
    document.querySelector('.result-container').style.display = 'block';
}, false );