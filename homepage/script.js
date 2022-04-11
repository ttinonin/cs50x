function mudaCor(){
    let lista = document.getElementById("daniel");
    let lista2 = document.getElementById("daniel2");
    let lista3 = document.getElementById("daniel3");
    let cor = document.getElementById("favcolor");
    lista.style.backgroundColor = cor.value;
    lista2.style.backgroundColor = cor.value;
    lista3.style.backgroundColor = cor.value;
}