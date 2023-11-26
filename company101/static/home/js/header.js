var header_icon_div = document.querySelector('#header_icon_div');
var header_nav_ui = document.querySelector('#header_nav_ui');

var mediaQuery = window.matchMedia("(max-width: 480px)");

if (mediaQuery.matches) {
    header_nav_ui.style.display = 'none';
}else{
    header_nav_ui.style.display = 'grid';
}

mediaQuery.addEventListener('change', function(event) {
    if (mediaQuery.matches) {
        header_nav_ui.style.display = 'none';
    }else{
        header_nav_ui.style.display = 'grid';
    }
});



header_icon_div.addEventListener('click', function(event) {
    if (header_nav_ui.style.display == 'none') {
        header_nav_ui.style.display = 'grid';
    }else{
        header_nav_ui.style.display = 'none';
    }
});


// element.style.cssText = 'color: blue; border: 1px solid black'
// element.setAttribute('style', 'color:red; border: 1px solid blue;')