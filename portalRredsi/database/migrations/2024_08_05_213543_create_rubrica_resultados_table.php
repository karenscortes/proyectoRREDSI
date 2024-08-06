<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('rubrica_resultados', function (Blueprint $table) {
            $table->unsignedBigInteger('id_rubrica_resultado')->primary()->autoIncrement();
            $table->float('puntaje_aprobacion',1);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('rubrica_resultados');
    }
};
