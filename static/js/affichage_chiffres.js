function formater_nombre(nombre){
    nombre = Number.parseFloat(nombre).toFixed(2); //toFixed(n) arrondit un NumberObj au nombre n après la virgule
    nombre = String(nombre);
    var x = nombre.split('.'); // séparer le string du nombre entre part entière et décimale
    var x1 = x[0]; // x1 part entière
    var x2 = x.length > 1 ? '.' + x[1] : ''; // x2 part décimale
    var rgx = /(\d+)(\d{3})/; // regex : avant la part décimale et tous les 3 chiffres
    while (rgx.test(x1)) { // tant qu'on est avant la part décimale et tous les trois chiffres
    x1 = x1.replace(rgx, '$1' + ' ' + '$2'); // insertion des espaces entre les blocs de 3 chiffres
    }
    return (x1 + x2 + ' Watts'); // on renvoie la part entière espacée et la part décimale avec son point et on ajoute l'unité. 
   }

var nombre = document.getElementById("nombre").innerHTML

if (nombre == '') {
// Ne rien faire si la string nombre est vide (cela signifie qu'aucun contenu n'a été envoyé par le script python au html)
}
else { // Si nombre pas vide, espacer tous les 3 chiffres et arrondir à la deuxième décimale 
    nombre = formater_nombre(nombre);
    document.getElementById("nombre").innerHTML = nombre;    
}
