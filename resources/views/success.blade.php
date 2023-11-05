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
            Gerador de Matriz Curricular - Matriz Gerada!
        </h1>
    </header>

    <div class="div-success">
        <p class="title-success">Grade gerada com sucesso!</p>
        <p class="description-success">A grade foi gerada com sucesso e foi exportada para sua pasta Downloads!</p>

        <div class="footer-success">
            <p>Caso o download não tenha iniciado automaticamente, clique no botão ao lado.</p>
            <div class="div-btn-partial-solution">
                <button id="btn-final-solution" onclick="window.location='{{url('main/download-solution')}}'">
                    <img src="{{ asset('img/download_icon.png') }}" alt="ícone de download" width="15" height="15">
                    Baixar Grade
                </button>
            </div>
        </div>
    </div>
</body>

</html>
