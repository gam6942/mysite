// API call MKT_3: Exporter un nombre de collectes des depenses pour chaque categorie de vetement

export function mkt_3() {

    function id(id) {return document.getElementById(id)}

    id("btn_exporter_mkt_3").onclick = ()=>{

        const value = id("inp_mkt_3").value

        if(value > 10000000 || value < 0){
            return;
        }

        fetch("https://guillaumem.pythonanywhere.com", {
            method: "POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify({mkt_3:value}),
        })
        .then(resp => resp.blob())
        .then(blob => {
            const dl = document.createElement("a")
            dl.href = window.URL.createObjectURL(blob)
            dl.download = "collecte.csv"
            dl.style.display = "none"
            document.body.appendChild(dl)
            dl.click()
            dl.remove()
        })
    }
}