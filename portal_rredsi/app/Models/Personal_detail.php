<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Personal_detail extends Model
{
    use HasFactory;
    protected $fillable = [
        'id_personal_detail',
        'id_document_type',
        'id_user',
        'document',
        'names',
        'last_names',
        'cell_phone',
        'id_institution',
    ];
}
