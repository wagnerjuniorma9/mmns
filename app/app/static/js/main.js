
const PLACE_HOLDER_NEWSLETTER = "digite seu e-mail"

$(document).ready(function () {

    //Realizar execucao de funcoes com custon button
    $(".btn-monteiro").click(function (element) {
        console.log(this.getAttribute('data-btn'))
    })

    // FORM NEWSLETTER paceholder manual
    $("#newsletterform").keypress(function () {

        let value = this.innerHTML.trim()

        if (value == PLACE_HOLDER_NEWSLETTER) {
            this.innerHTML = ""
        }

    })
    $("#newsletterform").blur(function () {

        let value = this.innerHTML.trim()

        if (value == "") {
            this.innerHTML = PLACE_HOLDER_NEWSLETTER
        }

    })

});