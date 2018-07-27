
$(document).ready(function () {

    //Realizar execucao de funcoes com custon button
    $(".btn-monteiro").click(function (element) {
        console.log(this.getAttribute('data-btn'))
    })

});