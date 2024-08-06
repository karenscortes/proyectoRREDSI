<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Phase_programming extends Model
{
    use HasFactory;
    protected $fillable = [
        'id_phase_programming', 
        'id_phase',
        'id_announcement',
        'start_dates',
        'end_dates',
    ]; 
}
