function erro(){
    let btn1 = document.getElementById("errado1");
    let respo = document.getElementById("resp");
    btn1.style.backgroundColor = "red";
    respo.innerHTML = "Incorect";
}

function erro2(){
    let btn2 = document.getElementById("errado2");
    let respo = document.getElementById("resp");
    btn2.style.backgroundColor = "red";
    respo.innerHTML = "Incorect";
}

function erro3(){
    let btn3 = document.getElementById("errado3");
    let respo = document.getElementById("resp");
    btn3.style.backgroundColor = "red";
    respo.innerHTML = "Incorect";
}

function cert(){
    let btn = document.getElementById("certo");
    let respo = document.getElementById("resp");
    btn.style.backgroundColor = "green";
    respo.innerHTML = "Correct!";
}

function submit(){
    let anwser = document.getElementById("caixa");
    let camp = document.getElementById("awn");
    if(anwser.value == 36){
        camp.innerHTML = "Correct!";
        anwser.style.backgroundColor = "lightgreen";
    }
    else{
        camp.innerHTML = "Incorrect";
        anwser.style.backgroundColor = "lightcoral";
    }
}
