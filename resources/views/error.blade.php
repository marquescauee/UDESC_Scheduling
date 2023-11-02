<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="{{ asset('css/style.css') }}" rel="stylesheet">
    <title>UDESC Scheduling</title>
</head>

<body>
    <header>
        <h1 id="header-title">
            Gerador de Matriz Curricular - Ocorreu um Erro
        </h1>
    </header>

    <div class="div-error">
        <p class="title-error">Não foi possível gerar a matriz curricular</p>
        <p class="description-error">Existem muitas Hards Constraints que não foram possíveis de serem cumpridas, tente gerar novamente ou considere diminuir o numero de Hards Constraints.</p>

        <div class="footer-error">
            <p>Caso queira analisar quais Hard Constraints não foram cumpridas, baixe o arquivo com a solução parcial.</p>
            <div class="div-btn-partial-solution">
                <button id="btn-partial-solution">
                    <img src="{{ asset('img/download_icon.png') }}" alt="ícone de download" width="15" height="15">
                    Solução Parcial
                </button>
            </div>
        </div>
    </div>
</body>

</html>
