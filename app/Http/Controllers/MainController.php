<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Redirect;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Storage;
use robertogallea\LaravelPython\Services\LaravelPython;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;

class MainController extends Controller
{
    public function downloadProfessores()
    {
        return Storage::disk('public')->download('Professores.xlsx');
    }

    public function downloadDisciplinas()
    {
        return Storage::disk('public')->download('Disciplinas.xlsx');
    }

    public function generate(Request $request)
    {

        if (!$request->input('upload_professores') && !$request->input('upload_disciplinas')) {
            return Redirect::to('/')->with('message', 'Você ainda não adicionou as planilhas. Por favor, adicione-as.');
        }

        if (!$request->input('upload_professores')) {
            return Redirect::to('/')->with('message', 'Você não adicionou a planilha de professores. Por favor, adicione as duas planilhas novamente.');
        }

        if (!$request->input('upload_disciplinas')) {
            return Redirect::to('/')->with('message', 'Você não adicionou a planilha de disciplinas. Por favor, adicione as duas planilhas novamente.');
        }

        $command = 'python '. public_path().'\python\SimulatedAnnealing.py 2>&1';
        $output = shell_exec($command);

        dd($output);
    }
}
