// API call MKT_2: Voir le panier moyen des depenses en fonction de la classe socio-professionnelle

export function mkt_2() {

    function id(id) {return document.getElementById(id)}

    id("btn_afficher_mkt_2").onclick = ()=>{

        if(id("btn_afficher_mkt_2").innerHTML === "Afficher"){

            fetch("https://guillaumem.pythonanywhere.com", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({mkt_2:"afficher"}),
            })
            .then(resp => resp.text())
            .then(data => {
                id("ctn_mkt_2").innerHTML = data
                id("btn_afficher_mkt_2").innerHTML = "Masquer"
            })
        }
        if(id("btn_afficher_mkt_2").innerHTML === "Masquer"){
            id("ctn_mkt_2").innerHTML = ""
            id("btn_afficher_mkt_2").innerHTML = "Afficher"
        }
    }
}