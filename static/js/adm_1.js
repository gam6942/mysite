// API call ADM_1: Gerer l'acces aux fonctionnalites marketing

export function adm_1(){

    function id(id){return document.getElementById(id)}

    if (id("acces_mkt").innerHTML === "acces marketing: autorisation"){
        id("autoriser").innerHTML = "Interdire"
    }else{
        id("autoriser").innerHTML = "Autoriser"
    }

    id("autoriser").onclick = ()=>{

        if (id("autoriser").innerHTML === "Autoriser"){

            fetch("https://guillaumem.pythonanywhere.com", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({adm_1:"autoriser"})
            })
            .then(resp => resp.text())
            .then(data => {
                id("acces_mkt").innerHTML = data
                id("autoriser").innerHTML = "Interdire"
            })
        }
        if (id("autoriser").innerHTML === "Interdire"){

            fetch("https://guillaumem.pythonanywhere.com", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({adm_1:"interdire"})
            })
            .then(resp => resp.text())
            .then(data => {
                id("acces_mkt").innerHTML = data
                id("autoriser").innerHTML = "Autoriser"
            })
        }
    }
}