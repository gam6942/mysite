// API call d'authentification

async function main() {

    const {mkt_1} = await import("./mkt_1.js");
    const {mkt_2} = await import("./mkt_2.js");
    const {mkt_3} = await import("./mkt_3.js");
    const {adm_1} = await import("./adm_1.js");

    function id(id) {return document.getElementById(id)}

    id("btn_connexion").onclick = ()=> {
        const login = id("inp_login").value;
        const password = id("inp_password").value;

        if (login === "" || password === "") {
            return;
        }

        fetch("https://guillaumem.pythonanywhere.com", {
            method: "POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify({
                login:login,
                password:password
            })
        })
        .then(resp => resp.text())
        .then(ui => {

            id("ctn_role").innerHTML = ui;
            id("inp_login").value = "";
            id("inp_password").value = "";

            if(id("btn_afficher_mkt_1")){
                mkt_1();
            }
            if(id("btn_afficher_mkt_2")){
                mkt_2();
            }
            if(id("btn_exporter_mkt_3")){
                mkt_3();
            }
            if(id("autoriser")){
                adm_1();
            }
        })
    }
}
main()