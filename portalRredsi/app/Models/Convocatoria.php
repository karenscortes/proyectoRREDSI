<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Convocatoria extends Model
{
    use HasFactory;
    protected $fillable = [
        'id_convocatoria',
        'nombre',
        'fecha_inicio', 
        'fecha_fin',
        'estado',
    ];
}
