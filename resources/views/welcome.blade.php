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

        <form action="{{ url('main/generate') }}" method="POST">
            @csrf
            <div id="div-botoes-upload-template">
                <div class="image-upload">
                    <label for="file-input-upload-professores">
                        <img src="{{ asset('img/upload_icon.png') }}" alt="ícone de upload" />
                        <p class="upload-btn-label">Upload Professores</p>
                    </label>
                    <input id="file-input-upload-professores" type="file" name="upload_professores" />
                </div>

                <div class="image-upload">
                    <label for="file-input-upload-disciplinas">
                        <img src="{{ asset('img/upload_icon.png') }}" alt="ícone de upload" />
                        <p class="upload-btn-label">Upload Disciplinas</p>
                    </label>
                    <input id="file-input-upload-disciplinas" type="file" name="upload_disciplinas" />
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
        <div class="pop-up-error">
            {{ Session::get('message') }}
        </div>
    @endif


    {{-- <div class="pop-up-success">
        <p>Upload realizado com sucesso!</p>
    </div> --}}


    <div id="logo-udesc">
        <img src="{{ asset('img/logo.png') }}" alt="Logo Udesc">
    </div>
</body>

</html>
