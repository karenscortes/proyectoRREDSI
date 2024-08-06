<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Area_conocimiento extends Model
{
    use HasFactory;

    protected $fillable = [
        'id_area_conocimiento',
        'nombre',
    ];
}
