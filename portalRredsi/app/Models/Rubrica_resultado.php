<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Rubrica_resultado extends Model
{
    use HasFactory;
    protected $fillable = [
        'id_rubrica_resultado',
        'puntaje_aprobacion',
    ];
}
