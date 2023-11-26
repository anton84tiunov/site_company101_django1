var header_icon_div = document.querySelector('#header_icon_div');
var header_nav_ui = document.querySelector('#header_nav_ui');
var header_nav_li_search = document.querySelector('#header_nav_li_search');
var header_search_form = document.querySelector('#header_search_form');
var header_but_search = document.querySelector('#header_but_search');
var header_input_search = document.querySelector('#header_input_search');
var header_search_form_result = document.querySelector('#header_search_form_result');
var header_search_ul_result = document.querySelector('#header_search_ul_result');
var header_select_search = document.querySelector("#header_select_search");

var mediaQuery = window.matchMedia("(max-width: 480px)");

header_search_form.style.display = 'none';
header_search_form_result.style.display = 'none';
header_search_ul_result.innerHTML = '';


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

header_nav_li_search.addEventListener('click', function(event) {
    // alert('header_nav_li_search');
    if (header_search_form.style.display == 'none') {
        header_search_form.style.display = 'grid';
        // header_search_form_result.style.display = 'block';
    }else{
        header_search_form_result.style.display = 'none';
        header_search_form.style.display = 'none';
        header_input_search.value = "";
        header_search_ul_result.innerHTML = '';
    }
});



header_but_search.addEventListener('click', function(event) {
    // alert('header_nav_li_search');
    if (header_input_search.value) {
        var search_result = '';

        const data = { 
            "str": header_input_search.value,
            "select": header_select_search.value
          };
          
          fetch('/search/str/', {
            method: 'POST',
            headers: {
                // "X-CSRFToken": token,
                // 'X-CSRFToken': csrftoken,
                "Accept": "application/json",
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
          })
            .then((response) => response.json())
            .then((data) => {
                search_result = data;
                if (header_input_search.value) {
                    header_search_ul_result.innerHTML = '';
                    header_search_form_result.style.display = 'block';
                    if(header_select_search.value === "all" || header_select_search.value === "news" ){
                        if(search_result['news']){
                            search_result['news'].forEach(n => {
                                var li = document.createElement("li");
                                var a = document.createElement("a");
                                a.setAttribute("href",`/news/${n['id']}`);
                                a.appendChild(document.createTextNode(n['title']));
                                li.appendChild(a);
                                header_search_ul_result.appendChild(li);
                            });
                        }
                    }
                    if(header_select_search.value === "all" || header_select_search.value === "news" ){

                        if(search_result['product']){
                            search_result['product'].forEach(n => {
                                var li = document.createElement("li");
                                var a = document.createElement("a");
                                a.setAttribute("href",`/market/product/${n['id']}`);
                                a.appendChild(document.createTextNode(n['model']));
                                li.appendChild(a);
                                header_search_ul_result.appendChild(li);
                            });
                        }
                    }
                    if(header_select_search.value === "all" || header_select_search.value === "service" ){

                        if(search_result['service']){
                            search_result['service'].forEach(n => {
                                var li = document.createElement("li");
                                var a = document.createElement("a");
                                a.setAttribute("href",`/service/service/${n['id']}`);
                                a.appendChild(document.createTextNode(n['name']));
                                li.appendChild(a);
                                header_search_ul_result.appendChild(li);
                            });
                        }
                    }
                }else{
                    header_search_form_result.style.display = 'none';
                    header_search_ul_result.innerHTML = '';
                }
            })
            .catch((error) => {
              console.log('Error:', error);
            });
    
      
    }else{
        header_search_form_result.style.display = 'none';
        header_search_ul_result.innerHTML = '';
    }


});



// element.style.cssText = 'color: blue; border: 1px solid black'
// element.setAttribute('style', 'color:red; border: 1px solid blue;')