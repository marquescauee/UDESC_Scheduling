<?php

use Illuminate\Support\Facades\Route;


Route::get('/', function () {
    return view('welcome');
});

Route::get('/loading', function () {
    return view('loading');
});

Route::get('/error', function () {
    return view('/error');
});

Route::get('/success', function () {
    return view('/success');
});

Route::get('main/download-professores', [\App\Http\Controllers\MainController::class, 'downloadProfessores']);

Route::get('main/download-disciplinas', [\App\Http\Controllers\MainController::class, 'downloadDisciplinas']);

Route::post('main/generate', [\App\Http\Controllers\MainController::class, 'generate']);
