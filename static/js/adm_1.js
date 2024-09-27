// API call ADM_1: Gerer l'acces aux fonctionnalites marketing

export function adm_1(){

    function id(id){return document.getElementById(id)}

    if (id("acces_mkt").innerHTML === "acces marketing: autorisation"){
        id("btn_autoriser").innerHTML = "Interdire"
    }else{
        id("btn_autoriser").innerHTML = "Autoriser"
    }

    id("btn_autoriser").onclick = ()=>{

        if (id("btn_autoriser").innerHTML === "Autoriser"){

            fetch("https://guillaumem.pythonanywhere.com", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({adm_1:"autoriser"})
            })
            .then(resp => resp.text())
            .then(data => {
                id("acces_mkt").innerHTML = data
                id("btn_autoriser").innerHTML = "Interdire"
            })
        }
        if (id("btn_autoriser").innerHTML === "Interdire"){

            fetch("https://guillaumem.pythonanywhere.com", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({adm_1:"interdire"})
            })
            .then(resp => resp.text())
            .then(data => {
                id("acces_mkt").innerHTML = data
                id("btn_autoriser").innerHTML = "Autoriser"
            })
        }
    }
}