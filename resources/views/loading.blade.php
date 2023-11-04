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

    <div class="loading-div">
        <p class="paragraph-generating">Gerando Matriz, isso pode demorar um pouco...</p>
        <div class="loader">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
        </div>
    </div>

    @php
        $result = shell_exec($command);
    @endphp

    @if (isset($result))
        <script>
            window.location.href = '/success'
        </script>
    @else
        <script>
            window.location.href = '/error'
        </script>
    @endif

</body>

</html>
