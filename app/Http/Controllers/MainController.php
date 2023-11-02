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
        $command = 'python '. public_path().'\python\SimulatedAnnealing.py 2>&1';
        $output = shell_exec($command);

        dd($output);
    }
}
