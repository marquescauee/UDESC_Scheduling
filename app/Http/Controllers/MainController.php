<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\File;
use Illuminate\Support\Facades\Redirect;
use Illuminate\Support\Facades\Response;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Storage;
use robertogallea\LaravelPython\Services\LaravelPython;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;
use Zip;

class MainController extends Controller
{
    public function downloadProfessores()
    {
        return Storage::disk('templates')->download('Professores.xls');
    }

    public function downloadDisciplinas()
    {
        return Storage::disk('templates')->download('Disciplinas.xls');
    }

    public function downloadSolution()
    {
        if (Storage::disk('full_solution')->exists("Solucao_Completa_Matriz_Professores.xls")) {
            $zip = Zip::create('matrizes_completa.zip');
            $zip->add(base_path().'/storage/app/public/full_solution', true);

            $zip->close();

            return Response::download(public_path('matrizes_completa.zip'));
        } else {
            $zip = Zip::create('matrizes_parcial.zip');
            $zip->add(base_path().'/storage/app/public/partial_solution', true);

            $zip->close();

            return Response::download(public_path('matrizes_parcial.zip'));
        }
    }

    public function generate(Request $request)
    {
        if (!$request->file('upload_professores') || !$request->file('upload_disciplinas')) {
            return Redirect::to('/')->with('message', 'Alguma planilha não foi adicionada. Por favor, adicione as duas planilhas novamente.');
        }

        $planilha_professores_extension = explode('.', $request['upload_professores']->getClientOriginalName())[1];

        $planilha_disciplinas_extension = explode('.', $request['upload_disciplinas']->getClientOriginalName())[1];

        $planilha_professores_name = $request['upload_professores']->getClientOriginalName();
        $planilha_disciplinas_name = $request['upload_disciplinas']->getClientOriginalName();

        File::put(base_path() . '/public/python/planilhas/Professores.' . $planilha_professores_extension, File::get($request->file('upload_professores')));

        File::put(base_path() . '/public/python/planilhas/Disciplinas.' . $planilha_disciplinas_extension, File::get($request->file('upload_disciplinas')));

        $command = "python " . public_path() . "/python/SimulatedAnnealing.py 2>&1 $planilha_professores_name $planilha_disciplinas_name";

        dd(shell_exec($command));

        return view('loading', compact('command'));
    }
}
