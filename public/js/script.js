
$(".js-file-upload-professores").on("change", function(e) {
    $(".pop-up-success").show('slow')

    if($(".pop-up-error")) {
        $(".pop-up-error").hide()
    }

    setTimeout(() => {
        $(".pop-up-success").fadeOut()
    }, 2000)
});

$(".js-file-upload-disciplinas").on("change", function(e) {
    $(".pop-up-success").show('slow')

    if($(".pop-up-error")) {
        $(".pop-up-error").hide()
    }

    setTimeout(() => {
        $(".pop-up-success").fadeOut()
    }, 2000)
});

function showPopUpError() {
    if(document.querySelector(".pop-up-error")) {
        setTimeout(() => {
            $(".pop-up-error").fadeOut()
        }, 4000)
    }
}

$("#btn-start-matriz-curricular").click(function(e) {

    if($(".js-file-upload-professores").get(0).files.length === 0 && $(".js-file-upload-disciplinas").get(0).files.length === 0) {
        e.preventDefault()
        $(".pop-up-error").show('slow')
        $(".error-message").text('Você ainda não adicionou as planilhas. Por favor, adicione-as.')
    } else if($(".js-file-upload-professores").get(0).files.length === 0) {
        e.preventDefault()
        $(".pop-up-error").show('slow')
        $(".error-message").text('Você não adicionou a planilha de professores. Por favor, adicione-a.')
    } else if($(".js-file-upload-disciplinas").get(0).files.length === 0) {
        e.preventDefault()
        $(".pop-up-error").show('slow')
        $(".error-message").text('Você não adicionou a planilha de disciplinas. Por favor, adicione-a.')
    }

    if($(".pop-up-success")) {
        $(".pop-up-success").hide()
    }
});

showPopUpError()
