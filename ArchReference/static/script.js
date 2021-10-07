window.onload = () => {
    
    $("#search").keyup(search_confirm)
}





function search_confirm(e){
    if(e.key == 'Enter' || e.keyCode === 13)
    {
        let query = $("#search").val()
        let category = $("input[name='categorias']:checked").val()
        let movement = $("input[name='movimentos']:checked").val()
        let climate = $("input[name='climas']:checked").val()
        let color = $("input[name='cores']:checked").val()
        let material = $("input[name='materiais']:checked").val()
        let area = $("input[name='areas']:checked").val()
        let filters = {query, category, movement, climate, color, material, area }
        console.log(filters);
        do_search(filters)
    }
}

function do_search(filters){
    let url = "http://192.168.0.187:3000/searchProjects"
    $.post(url,filters, ()=>{
        console.log("fiz")
    }).done((data) => {
        console.log(data)
        build_list(data)
    })
}

function build_list(data){
    var lista = "";
    data.projects.forEach(p => {
        lista += build_card(p);
    });
    console.log(lista)
    $("#cards").html(() =>{
        return lista
    })
}

function build_card(project){
    let card = 
    '<li>'+
        '<a href="'+project.link+'" target="_blank" class="card">'+
        '<img src="'+project.thumb+'" class="card__image" alt="" />'+
        '<div class="card__overlay">'+
            '<div class="card__header">'+
            '<div class="card__header-text">'+
                '<h3 class="card__title">'+project.title+'</h3>'+
                '<span class="card__status">1 hour ago</span>'+
            '</div>'+
            '</div>'+
            
        '</div>'+
        '</a>'+  
    '</li>'
    return card
}