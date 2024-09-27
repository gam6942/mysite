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

            if (id("nb_collecte")){
                mkt_1();
                mkt_2();
                mkt_3();
            }
            if(id("acces_mkt")){
                adm_1();
            }
        })
    }
}
main()