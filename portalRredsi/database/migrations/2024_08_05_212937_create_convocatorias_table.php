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
        Schema::create('convocatorias', function (Blueprint $table) {
            $table->unsignedBigInteger('id_convocatoria')->primary()->autoIncrement();
            $table->string('nombre',25); 
            $table->date('fecha_inicio'); 
            $table->date('fecha_fin'); 
            $table->enum('estado',['en curso','concluido','por publicar']); 
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('convocatorias');
    }
};
