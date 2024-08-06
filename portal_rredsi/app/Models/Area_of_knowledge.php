<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Area_of_knowledge extends Model
{
    use HasFactory;
    protected $fillable = [
        'id_area_of_knowledge',
        'names',
    ];
}
