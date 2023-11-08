<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\File;
use Illuminate\Support\Facades\Redirect;
use Illuminate\Support\Facades\Response;
use Illuminate\Support\Facades\Storage;
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

        $zip = Zip::create('solucao.zip');
        $zip->add(base_path() . '/storage/app/public/solution', true);

        $zip->close();

        return Response::download(public_path('solucao.zip'));

    }

    public function generate(Request $request)
    {
        if (!$request->file('upload_professores') || !$request->file('upload_disciplinas')) {
            return Redirect::to('/')->with('message', 'Alguma planilha não foi adicionada. Por favor, adicione as duas planilhas novamente.');
        }

        $planilha_professores_name = $request['upload_professores']->getClientOriginalName();
        $planilha_disciplinas_name = $request['upload_disciplinas']->getClientOriginalName();

        File::put(base_path() . '/public/python/planilhas/'. $planilha_professores_name, File::get($request->file('upload_professores')));

        File::put(base_path() . '/public/python/planilhas/'. $planilha_disciplinas_name, File::get($request->file('upload_disciplinas')));

        $command = "python " . public_path() . "/python/SimulatedAnnealing.py 2>&1 $planilha_professores_name $planilha_disciplinas_name";

        ini_set('max_execution_time', 3600);
        ini_set('max_input_time', -1);
        set_time_limit(3600);

        return shell_exec($command);
    }
}
