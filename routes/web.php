<?php

use Illuminate\Http\Client\Request;
use Illuminate\Support\Facades\Route;


Route::get('/', function () {
    return view('welcome');
});

Route::get('/error', function () {
    return view('/error');
})->name('error');

Route::get('/success', function () {
    return view('/success');
})->name('success');

Route::get('main/download-professores', [\App\Http\Controllers\MainController::class, 'downloadProfessores']);

Route::get('main/download-disciplinas', [\App\Http\Controllers\MainController::class, 'downloadDisciplinas']);

Route::post('main/generate', [\App\Http\Controllers\MainController::class, 'generate']);

Route::get('main/download-solution', [\App\Http\Controllers\MainController::class, 'downloadSolution']);
