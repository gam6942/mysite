// API call MKT_1: Voir les depenses par categorie de vetement en fonction de la classe socio-professionnelle

export function mkt_1() {

    function id(id) {return document.getElementById(id)}

    id("btn_afficher_mkt_1").onclick = ()=>{

        if(id("btn_afficher_mkt_1").innerHTML === "Afficher"){

            fetch("https://guillaumem.pythonanywhere.com", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({mkt_1:"afficher"}),
            })
            .then(resp => resp.text())
            .then(data => {
                id("ctn_mkt_1").innerHTML = data
                id("btn_afficher_mkt_1").innerHTML = "Masquer"
            })
        }
        if(id("btn_afficher_mkt_1").innerHTML === "Masquer"){
            id("ctn_mkt_1").innerHTML = ""
            id("btn_afficher_mkt_1").innerHTML = "Afficher"
        }

    }
}