
$(".js-file-upload-professores").on("change", function (e) {
    if ($(".js-file-upload-professores").get(0).files.length === 0) {
        return
    }

    $(".pop-up-success").show('slow')

    if ($(".pop-up-error")) {
        $(".pop-up-error").hide()
    }

    setTimeout(() => {
        $(".pop-up-success").fadeOut()
    }, 2000)
});

$(".js-file-upload-disciplinas").on("change", function (e) {
    if ($(".js-file-upload-disciplinas").get(0).files.length === 0) {
        return
    }

    $(".pop-up-success").show('slow')

    if ($(".pop-up-error")) {
        $(".pop-up-error").hide()
    }

    setTimeout(() => {
        $(".pop-up-success").fadeOut()
    }, 2000)
});

function showPopUpError() {
    if (document.querySelector(".pop-up-error")) {
        setTimeout(() => {
            $(".pop-up-error").fadeOut()
        }, 4000)
    }
}

$("#btn-start-matriz-curricular").click(function (e) {

    if ($(".js-file-upload-professores").get(0).files.length === 0 && $(".js-file-upload-disciplinas").get(0).files.length === 0) {
        e.preventDefault()
        $(".pop-up-error").show('slow')
        $(".error-message").text('Você ainda não adicionou as planilhas. Por favor, adicione-as.')
        showPopUpError()
    } else if ($(".js-file-upload-professores").get(0).files.length === 0) {
        e.preventDefault()
        $(".pop-up-error").show('slow')
        $(".error-message").text('Você não adicionou a planilha de professores. Por favor, adicione-a.')
        showPopUpError()
    } else if ($(".js-file-upload-disciplinas").get(0).files.length === 0) {
        e.preventDefault()
        $(".pop-up-error").show('slow')
        $(".error-message").text('Você não adicionou a planilha de disciplinas. Por favor, adicione-a.')
        showPopUpError()
    }

    if ($(".pop-up-success")) {
        $(".pop-up-success").hide()
    }
});

function handleSubmit() {
    let upload_professores;
    let upload_disciplinas;

    $(document).ready(function () {

        $('#file-input-upload-professores').change(function (e) {
            upload_professores = $('#file-input-upload-professores')[0].files[0];
        });

        $('#file-input-upload-disciplinas').change(function (e) {
            upload_disciplinas = $('#file-input-upload-disciplinas')[0].files[0];
        });

        $("#form-start-matriz-curricular").on('submit', function () {
            $(".main-div").empty()
            $(".main-div").append('<div class="loading-div"><p class="paragraph-generating">Gerando Matriz. Isso pode demorar um pouco...</p><span class="loader"></span></div>')

            $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content'),
                    'Access-Control-Allow-Origin': 'http://127.0.0.1:8000'
                }
            });

            const formData = new FormData();
            formData.append('upload_professores', upload_professores)
            formData.append('upload_disciplinas', upload_disciplinas)

            $.ajax({
                data: formData,
                type: "POST",
                url: "http://127.0.0.1:8000/main/generate",
                cache: false,
                contentType: false,
                processData: false,
                success: function (result) {
                    if (result.trim() === 'ERRO DE PLANILHA') {
                        $(".paragraph-generating").css("color", "#cc3300")
                        $(".paragraph-generating").text('Há um erro de informações nas planilhas. Por favor, verifique-as e tente novamente. Você será redirecionado para a página principal em 5 segundos.')
                        $(".loader").css("display", "none")

                        setTimeout(() => {
                            window.location.href = '/'
                        }, 5000);
                    }
                    else if (result.trim() === '1')
                        window.location.href = '/success'
                    else
                        window.location.href = '/error'
                }

            });
        })
    });
}

$(".btn-download-final-answer").click(function (e) {
    if ($(".btn-download-final-answer").hasClass("disabled")) {
        e.preventDefault()
        $(".pop-up-error").show('slow')
        $(".error-message").text('Ainda não foi gerada uma solução. Por favor, adicione as planilhas e inicie a execução.')
    }

    if ($(".pop-up-success")) {
        $(".pop-up-success").hide()
    }
})

showPopUpError()
handleSubmit()
