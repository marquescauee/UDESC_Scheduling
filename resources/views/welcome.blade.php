<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="{{ asset('css/style.css') }}" rel="stylesheet">
    <script src="{{ asset('js/script.js') }}" defer></script>
    <title>UDESC Scheduling</title>
</head>

<body>
    <header>
        <h1 id="header-title">
            Gerador de Matriz Curricular - Engenharia de Software - UDESC
        </h1>
    </header>

    <div class="main-div">
        <div id="div-botoes-download-template">
            <button id="btn-download-professores" type="button"
                onclick="window.location='{{ url('main/download-professores') }}'">
                <img src="{{ asset('img/download_icon.png') }}" alt="ícone de download" width="15" height="15">
                Download Template
            </button>
            <button id="btn-download-disciplinas" type="button"
                onclick="window.location='{{ url('main/download-disciplinas') }}'">
                <img src="{{ asset('img/download_icon.png') }}" alt="ícone de download" width="15" height="15">
                Download Template
            </button>
        </div>

        <form action="{{ url('main/generate') }}" method="POST" enctype="multipart/form-data">
            @csrf
            <div id="div-botoes-upload-template">
                <div class="image-upload">
                    <label for="file-input-upload-professores">
                        <img src="{{ asset('img/upload_icon.png') }}" alt="ícone de upload" />
                        <p class="upload-btn-label">Upload Professores</p>
                    </label>
                    <input id="file-input-upload-professores" class="js-file-upload-professores" type="file"
                        name="upload_professores" />
                </div>

                <div class="image-upload">
                    <label for="file-input-upload-disciplinas">
                        <img src="{{ asset('img/upload_icon.png') }}" alt="ícone de upload" />
                        <p class="upload-btn-label">Upload Disciplinas</p>
                    </label>
                    <input id="file-input-upload-disciplinas" class="js-file-upload-disciplinas" type="file"
                        name="upload_disciplinas" />
                </div>
            </div>


            <div class="container-start-and-download">
                <button type="submit" id="btn-start-matriz-curricular">
                    <img src="{{ asset('img/plus_circle_icon.png') }}" alt="Ícone de adição">
                    Gerar Matriz Curricular
                    <img src="{{ asset('img/plus_circle_icon.png') }}" alt="Ícone de adição">
                </button>
                @if (!Storage::disk('public')->exists('Solution.xlsx'))
                    <button id="btn-download-final-answer" disabled style="opacity: 0.5">
                        <img src="{{ asset('img/download_answer.png') }}" alt="Donwload Answer">
                    </button>
                @else
                    <button id="btn-download-final-answer">
                        <img src="{{ asset('img/download_answer.png') }}" alt="Donwload Answer">
                    </button>
                @endif
            </div>
        </form>
    </div>

    @if (Session::has('message'))
        <div class="pop-up-error" style="display: block;">
            <p class="error-message">{{ Session::get('message') }}</p>
        </div>
    @endif

    <div class="pop-up-error">
        <p class="error-message"></p>
    </div>

    <div class="pop-up-success">
        <p class="success-message">Upload realizado com sucesso!</p>
    </div>


    <div id="logo-udesc">
        <img src="{{ asset('img/logo.png') }}" alt="Logo Udesc">
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
</body>

</html>
