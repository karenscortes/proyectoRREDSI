<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Phase extends Model
{
    use HasFactory;
    protected $fillable = [
        'id_phase',
        'names',
        'id_stage',
    ];
}
