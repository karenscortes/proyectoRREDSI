<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Permission extends Model
{
    use HasFactory;
    protected $fillable = [
        'id_module',
        'id_role',
        'p_insert',
        'p_select',
        'p_update',
        'p_delete',
    ];
}
