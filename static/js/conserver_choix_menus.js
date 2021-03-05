var dep = localStorage.getItem("dep")
var reg = localStorage.getItem("reg")
var fil = localStorage.getItem("fil")

if(dep != null && reg !== null && fil != null){
    setValues(); // On update ici les valeurs des menus
}

function getValues(){
    var dep = document.getElementsByTagName("SELECT")[0].getAttribu //prend le premier élément "select" de la page
}